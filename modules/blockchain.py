"""
Blockchain Ledger Module
Implements an append-only, cryptographic blockchain ledger for audit provenance and tamper detection.
"""

import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from modules.hashing import IntegrityHasher
from config.settings import LEDGER_PATH

class Block:
    """Represents an immutable block in the transformation ledger."""

    def __init__(
        self,
        index: int,
        timestamp: float,
        previous_hash: str,
        data: Dict[str, Any],
        block_hash: Optional[str] = None
    ):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.hash = block_hash or self.calculate_hash()

    def calculate_hash(self) -> str:
        """Computes the SHA-256 hash of the block contents."""
        block_payload = {
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "data": self.data
        }
        return IntegrityHasher.hash_dict(block_payload)

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the block to a dictionary."""
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "data": self.data,
            "hash": self.hash
        }

    @classmethod
    def from_dict(cls, data_dict: Dict[str, Any]) -> "Block":
        """Instantiates a Block from a serialized dictionary."""
        return cls(
            index=data_dict["index"],
            timestamp=data_dict["timestamp"],
            previous_hash=data_dict["previous_hash"],
            data=data_dict["data"],
            block_hash=data_dict["hash"]
        )


class BlockchainLedger:
    """Manages the append-only cryptographic ledger with persistent storage."""

    def __init__(self, ledger_file: str = LEDGER_PATH):
        self.ledger_file = Path(ledger_file)
        self.chain: List[Block] = []
        self.load_or_initialize()

    def create_genesis_block(self) -> Block:
        """Creates the foundational Genesis Block."""
        genesis_data = {
            "event": "GENESIS_INITIALIZATION",
            "organization": "National Technical Research Organisation (NTRO)",
            "system": "Gen AI Content Transformation & Cryptographic Audit Ledger",
            "security_policy": "Zero-Trust Data Isolation & SHA-256 Chaining"
        }
        genesis_block = Block(
            index=0,
            timestamp=1700000000.0,  # Deterministic base timestamp
            previous_hash="0" * 64,
            data=genesis_data
        )
        return genesis_block

    def load_or_initialize(self) -> None:
        """Loads existing ledger from disk or creates a new genesis chain."""
        if self.ledger_file.exists():
            try:
                with open(self.ledger_file, "r", encoding="utf-8") as f:
                    serialized_chain = json.load(f)
                self.chain = [Block.from_dict(b) for b in serialized_chain]
                if not self.chain:
                    self._init_fresh_chain()
            except Exception:
                self._init_fresh_chain()
        else:
            self._init_fresh_chain()

    def _init_fresh_chain(self) -> None:
        """Initializes and persists a fresh genesis block."""
        self.chain = [self.create_genesis_block()]
        self.save_to_disk()

    def save_to_disk(self) -> None:
        """Persists the blockchain to disk."""
        self.ledger_file.parent.mkdir(parents=True, exist_ok=True)
        serialized_chain = [b.to_dict() for b in self.chain]
        with open(self.ledger_file, "w", encoding="utf-8") as f:
            json.dump(serialized_chain, f, indent=2)

    def get_latest_block(self) -> Block:
        """Returns the most recently appended block."""
        return self.chain[-1]

    def add_transformation_block(
        self,
        transformation_id: str,
        source_name: str,
        source_hash: str,
        output_hashes: Dict[str, str],
        config_metadata: Dict[str, Any],
        security_status: str
    ) -> Block:
        """
        Creates and appends a new transaction block for a content transformation event.
        """
        latest_block = self.get_latest_block()
        transaction_data = {
            "transformation_id": transformation_id,
            "source_name": source_name,
            "source_hash": source_hash,
            "output_hashes": output_hashes,
            "artefact_count": len(output_hashes),
            "config": config_metadata,
            "security_status": security_status
        }

        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            previous_hash=latest_block.hash,
            data=transaction_data
        )

        self.chain.append(new_block)
        self.save_to_disk()
        return new_block

    def verify_chain_integrity(self) -> Tuple[bool, Optional[str], Optional[int]]:
        """
        Validates the entire cryptographic chain:
        1. Checks that each block's internal hash matches its calculated hash.
        2. Checks that each block's previous_hash matches the previous block's hash.
        
        Returns (is_valid, error_message, compromised_block_index).
        """
        if not self.chain:
            return False, "Ledger is empty", None

        # Verify Genesis Block
        if self.chain[0].previous_hash != "0" * 64:
            return False, "Genesis block previous_hash is invalid", 0

        if self.chain[0].hash != self.chain[0].calculate_hash():
            return False, "Genesis block hash has been corrupted", 0

        # Verify Sequential Linkage
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # 1. Verify recalculation
            if current.hash != current.calculate_hash():
                return False, f"Block #{current.index} hash mismatch (content modified)", current.index

            # 2. Verify link to previous
            if current.previous_hash != previous.hash:
                return False, f"Block #{current.index} previous_hash does not match Block #{previous.index} hash", current.index

        return True, "Ledger integrity verified: All blocks cryptographically valid.", None

    def get_chain_summary(self) -> Dict[str, Any]:
        """Returns statistics and summary of the blockchain."""
        is_valid, msg, bad_index = self.verify_chain_integrity()
        return {
            "total_blocks": len(self.chain),
            "genesis_hash": self.chain[0].hash if self.chain else None,
            "latest_block_hash": self.get_latest_block().hash if self.chain else None,
            "is_valid": is_valid,
            "verification_status": msg,
            "compromised_index": bad_index
        }
