"""
History & Persistence Module
SQLite-backed storage and retrieval for transformation events and audit trails.
"""

import sqlite3
import json
import uuid
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from config.settings import DB_PATH

class TransformationHistoryDB:
    """Manages SQLite database operations for transformation audit logs."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_tables()

    def _get_connection(self) -> sqlite3.Connection:
        """Returns a configured SQLite connection."""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_tables(self) -> None:
        """Initializes database schema if not present."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transformations (
                    id TEXT PRIMARY KEY,
                    timestamp REAL NOT NULL,
                    created_at_str TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    source_type TEXT NOT NULL,
                    source_hash TEXT NOT NULL,
                    source_preview TEXT NOT NULL,
                    security_status TEXT NOT NULL,
                    security_report TEXT NOT NULL,
                    config TEXT NOT NULL,
                    selected_outputs TEXT NOT NULL,
                    outputs TEXT NOT NULL,
                    output_hashes TEXT NOT NULL,
                    block_index INTEGER,
                    block_hash TEXT
                )
            """)
            conn.commit()

    def save_transformation(
        self,
        source_name: str,
        source_type: str,
        source_hash: str,
        source_content: str,
        security_status: str,
        security_report: Dict[str, Any],
        config: Dict[str, Any],
        selected_outputs: List[str],
        outputs: Dict[str, str],
        output_hashes: Dict[str, str],
        block_index: int,
        block_hash: str,
        custom_id: Optional[str] = None
    ) -> str:
        """Saves a transformation event into the SQLite repository."""
        doc_id = custom_id or f"DOC-{int(time.time()) % 100000:05d}"
        now_ts = time.time()
        created_str = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(now_ts))
        preview = (source_content[:200] + "...") if len(source_content) > 200 else source_content

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO transformations (
                    id, timestamp, created_at_str, source_name, source_type,
                    source_hash, source_preview, security_status, security_report,
                    config, selected_outputs, outputs, output_hashes,
                    block_index, block_hash
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                doc_id,
                now_ts,
                created_str,
                source_name,
                source_type,
                source_hash,
                preview,
                security_status,
                json.dumps(security_report),
                json.dumps(config),
                json.dumps(selected_outputs),
                json.dumps(outputs),
                json.dumps(output_hashes),
                block_index,
                block_hash
            ))
            conn.commit()
        return doc_id

    def get_all(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Retrieves recent transformations ordered by newest first."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM transformations
                ORDER BY timestamp DESC
                LIMIT ?
            """, (limit,))
            rows = cursor.fetchall()

        results = []
        for row in rows:
            results.append({
                "id": row["id"],
                "timestamp": row["timestamp"],
                "created_at_str": row["created_at_str"],
                "source_name": row["source_name"],
                "source_type": row["source_type"],
                "source_hash": row["source_hash"],
                "source_preview": row["source_preview"],
                "security_status": row["security_status"],
                "security_report": json.loads(row["security_report"]),
                "config": json.loads(row["config"]),
                "selected_outputs": json.loads(row["selected_outputs"]),
                "outputs": json.loads(row["outputs"]),
                "output_hashes": json.loads(row["output_hashes"]),
                "block_index": row["block_index"],
                "block_hash": row["block_hash"]
            })
        return results

    def get_by_id(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves a specific transformation by its document ID."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transformations WHERE id = ?", (doc_id,))
            row = cursor.fetchone()

        if not row:
            return None

        return {
            "id": row["id"],
            "timestamp": row["timestamp"],
            "created_at_str": row["created_at_str"],
            "source_name": row["source_name"],
            "source_type": row["source_type"],
            "source_hash": row["source_hash"],
            "source_preview": row["source_preview"],
            "security_status": row["security_status"],
            "security_report": json.loads(row["security_report"]),
            "config": json.loads(row["config"]),
            "selected_outputs": json.loads(row["selected_outputs"]),
            "outputs": json.loads(row["outputs"]),
            "output_hashes": json.loads(row["output_hashes"]),
            "block_index": row["block_index"],
            "block_hash": row["block_hash"]
        }

    def get_total_count(self) -> int:
        """Returns total count of logged transformations."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM transformations")
            return cursor.fetchone()[0]
