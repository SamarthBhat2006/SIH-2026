"""
Unit tests for SHA-256 cryptographic hashing.
"""

import hashlib
from modules.hashing import IntegrityHasher

def test_hash_text_deterministic():
    text = "NTRO Cyber Incident Response Briefing"
    expected = hashlib.sha256(text.encode("utf-8")).hexdigest()
    assert IntegrityHasher.hash_text(text) == expected

def test_hash_dict_deterministic_keys():
    d1 = {"a": 1, "b": 2, "c": "test"}
    d2 = {"c": "test", "a": 1, "b": 2}
    # Keys in different order must yield identical SHA-256 digest
    assert IntegrityHasher.hash_dict(d1) == IntegrityHasher.hash_dict(d2)

def test_generate_artefact_hashes():
    outputs = {
        "summary": "Executive overview content",
        "advisory": "Cybersecurity advisory content"
    }
    hashes = IntegrityHasher.generate_artefact_hashes(outputs)
    assert len(hashes) == 2
    assert hashes["summary"] == IntegrityHasher.hash_text("Executive overview content")
    assert hashes["advisory"] == IntegrityHasher.hash_text("Cybersecurity advisory content")
