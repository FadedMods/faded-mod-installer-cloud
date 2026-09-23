#!/usr/bin/env python3
"""Sign packaged FJL artifacts without persisting the private key.

The Ed25519 private key is read exclusively from stdin. Accepted encodings are
PEM, DER, or base64-wrapped PEM/DER. The generated JSON contains only public
release metadata and signatures.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--release-base-url", required=True)
    parser.add_argument("--key-id", required=True)
    parser.add_argument("--expected-public-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def load_private_key(secret: bytes) -> Ed25519PrivateKey:
    normalized = secret.strip()
    candidates = [normalized]
    try:
        decoded = base64.b64decode(normalized, validate=True)
        if decoded not in candidates:
            candidates.append(decoded)
    except (binascii.Error, ValueError):
        pass

    for candidate in candidates:
        for loader in (
            serialization.load_pem_private_key,
            serialization.load_der_private_key,
        ):
            try:
                key = loader(candidate, password=None)
            except (TypeError, ValueError):
                continue
            if not isinstance(key, Ed25519PrivateKey):
                raise SystemExit("The supplied private key is not an Ed25519 key.")
            return key
    raise SystemExit("Could not decode the Ed25519 private key from stdin.")


def public_fingerprint(key: Ed25519PrivateKey) -> str:
    public_der = key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return hashlib.sha256(public_der).hexdigest()


def atomic_write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, indent=2) + "\n").encode("utf-8")
    handle, temp_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(handle, "wb") as temp_file:
            temp_file.write(encoded)
            temp_file.flush()
            os.fsync(temp_file.fileno())
        os.replace(temp_name, path)
    finally:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass


def main() -> int:
    args = parse_args()
    secret = bytearray(sys.stdin.buffer.read())
    try:
        key = load_private_key(bytes(secret))
    finally:
        for index in range(len(secret)):
            secret[index] = 0

    actual_fingerprint = public_fingerprint(key)
    expected_fingerprint = args.expected_public_sha256.lower()
    if actual_fingerprint != expected_fingerprint:
        raise SystemExit(
            "Refusing to sign with an unexpected key: "
            f"expected {expected_fingerprint}, got {actual_fingerprint}."
        )

    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    artifacts: dict[str, object] = {}
    public_key: Ed25519PublicKey = key.public_key()
    for target, source in manifest["artifacts"].items():
        filename = source["file"]
        if Path(filename).name != filename or not filename:
            raise SystemExit(f"Invalid artifact filename: {filename}")
        artifact_path = args.release_dir / filename
        data = artifact_path.read_bytes()
        sha256 = hashlib.sha256(data).hexdigest()
        if source.get("sha256", "").lower() != sha256:
            raise SystemExit(f"Refusing to sign {filename}: packaged SHA-256 does not match")
        signature = key.sign(data)
        public_key.verify(signature, data)
        artifacts[target] = {
            "download_url": f"{args.release_base_url.rstrip('/')}/{filename}",
            "zip_name": filename,
            "size_bytes": len(data),
            "sha256": sha256,
            "signature": base64.b64encode(signature).decode("ascii"),
        }
        source["url"] = artifacts[target]["download_url"]
        source["signature"] = artifacts[target]["signature"]

    output = {
        "product": manifest["product"],
        "version": manifest["version"],
        "minimum_pz_build": manifest["minimumPZBuild"],
        "trusted_key_id": args.key_id,
        "public_key_sha256": actual_fingerprint,
        "artifacts": artifacts,
    }
    atomic_write_json(args.output, output)
    # Publishable metadata must describe exactly the bytes signed above. Previously this
    # script left release-manifest.json URLs/signatures as PLACEHOLDER, requiring a second
    # workflow with an obsolete key registry just to finalize an otherwise signed release.
    atomic_write_json(args.manifest, manifest)
    checksum_path = args.release_dir / "checksums.sha256"
    if checksum_path.is_file():
        names = [line.split(None, 1)[1].strip() for line in checksum_path.read_text(encoding="utf-8-sig").splitlines()
                 if line.strip()]
        if args.output.resolve().parent == args.release_dir.resolve() and args.output.name not in names:
            names.append(args.output.name)
        lines = []
        for name in names:
            path = args.release_dir / name
            if Path(name).name != name or not path.is_file():
                raise SystemExit(f"Invalid checksum artifact: {name}")
            lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {name}")
        checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
    print(f"Signed and verified {len(artifacts)} artifacts with {args.key_id}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
