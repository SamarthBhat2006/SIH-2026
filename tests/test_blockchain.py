"""
Unit tests for the blockchain ledger and tamper detection.
"""

import tempfile
import os
from modules.blockchain import BlockchainLedger

def test_blockchain_initialization():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        tmp_path = tmp.name

    try:
        ledger = BlockchainLedger(tmp_path)
        assert len(ledger.chain) == 1
        genesis = ledger.chain[0]
        assert genesis.index == 0
        assert genesis.previous_hash == "0" * 64
        
        is_valid, msg, bad_idx = ledger.verify_chain_integrity()
        assert is_valid is True
        assert bad_idx is None
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def test_add_transformation_block_and_verification():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        tmp_path = tmp.name

    try:
        ledger = BlockchainLedger(tmp_path)
        block = ledger.add_transformation_block(
            transformation_id="DOC-9999",
            source_name="incident_test.txt",
            source_hash="abcd1234efgh5678" * 4,
            output_hashes={"executive_summary": "1111222233334444" * 4},
            config_metadata={"audience": "Executive", "tone": "Formal"},
            security_status="CLEAN"
        )
        assert block.index == 1
        assert block.previous_hash == ledger.chain[0].hash
        assert len(ledger.chain) == 2

        # Verify integrity
        is_valid, msg, bad_idx = ledger.verify_chain_integrity()
        assert is_valid is True

        # Test tamper detection: modify block #1 payload
        ledger.chain[1].data["source_name"] = "tampered_file.txt"
        tamper_valid, tamper_msg, tamper_idx = ledger.verify_chain_integrity()
        assert tamper_valid is False
        assert tamper_idx == 1
        assert "mismatch" in tamper_msg.lower()
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
