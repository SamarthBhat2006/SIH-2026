"""
Hashing Module
Generates cryptographic SHA-256 fingerprints for sources, artefacts, and ledger blocks.
"""

import hashlib
import json
from typing import Dict, Any

class IntegrityHasher:
    """Calculates deterministic SHA-256 cryptographic hashes."""

    @staticmethod
    def hash_text(text: str) -> str:
        """Computes SHA-256 hexadecimal digest of a UTF-8 text string."""
        if not isinstance(text, str):
            text = str(text)
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    @staticmethod
    def hash_bytes(data: bytes) -> str:
        """Computes SHA-256 hexadecimal digest of raw bytes."""
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def hash_dict(data: Dict[str, Any]) -> str:
        """
        Computes SHA-256 hexadecimal digest of a dictionary using
        sorted JSON serialization for deterministic output.
        """
        serialized = json.dumps(data, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    @classmethod
    def generate_artefact_hashes(cls, outputs: Dict[str, str]) -> Dict[str, str]:
        """Calculates SHA-256 hashes for all generated output artefacts."""
        return {key: cls.hash_text(content) for key, content in outputs.items()}
