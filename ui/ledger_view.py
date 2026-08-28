"""
Blockchain Ledger & Integrity Explorer View Module
Visualizes the append-only cryptographic blockchain blocks and performs real-time tamper verification.
"""

import time
import streamlit as st
from modules.blockchain import BlockchainLedger
from ui.components import render_hash_badge

def render_ledger_view(ledger: BlockchainLedger) -> None:
    """Renders the Blockchain Ledger explorer and verification portal."""
    st.markdown("### ⛓️ Cryptographic Blockchain Ledger & Integrity Explorer")
    st.caption("Immutable append-only block ledger securing source-to-artefact provenance for NTRO operational integrity.")

    # Ledger Summary Statistics
    summary = ledger.get_chain_summary()
    is_valid, msg, bad_index = ledger.verify_chain_integrity()

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{summary['total_blocks']}</div>
            <div class="metric-title">Total Ledger Blocks</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        status_color = "#00e676" if is_valid else "#ff1744"
        status_text = "VERIFIED IMMUTABLE" if is_valid else "CORRUPTED / TAMPERED"
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value" style="color: {status_color}; font-size: 1.1rem;">{status_text}</div>
            <div class="metric-title">Cryptographic Integrity</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        latest = summary['latest_block_hash']
        disp_latest = (latest[:12] + "...") if latest else "N/A"
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value" style="font-size: 1.1rem; color: #58a6ff;">{disp_latest}</div>
            <div class="metric-title">Head Block Digest</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Verification Action Row
    col_v1, col_v2 = st.columns([2, 1])
    with col_v1:
        if st.button("🔐 Run Real-Time Cryptographic Ledger Verification", type="primary", use_container_width=True):
            with st.spinner("Calculating full chain SHA-256 recursive checksums..."):
                time.sleep(0.4)
                v_valid, v_msg, v_bad = ledger.verify_chain_integrity()
                if v_valid:
                    st.success(f"✓ {v_msg}")
                else:
                    st.error(f"❌ TAMPERING DETECTED: {v_msg} at Block #{v_bad}")

    with col_v2:
        if st.button("🔄 Reload Ledger From Disk", use_container_width=True):
            ledger.load_or_initialize()
            st.rerun()

    st.markdown("---")
    st.markdown("#### 🧱 Sequential Block Explorer")

    # Render Blocks in Reverse Chronological Order (Newest First)
    for block in reversed(ledger.chain):
        is_genesis = (block.index == 0)
        card_border = "border-left: 4px solid #00e676;" if is_genesis else "border-left: 4px solid #00e5ff;"
        block_type_label = "🌟 GENESIS BLOCK" if is_genesis else f"📦 TRANSFORMATION BLOCK #{block.index}"
        
        block_time_str = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(block.timestamp))

        with st.expander(f"{block_type_label} | Hash: {block.hash[:16]}... | {block_time_str}", expanded=(block.index == len(ledger.chain) - 1)):
            st.markdown(f"""
            <div style="padding: 0.5rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <strong style="color: #00e5ff;">Block #{block.index}</strong>
                    <span style="color: #8b949e; font-size: 0.8rem;">Timestamp: {block_time_str}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            render_hash_badge(block.hash, "Block Hash (SHA-256)")
            render_hash_badge(block.previous_hash, "Previous Block Link")

            st.markdown("**Block Transaction Payload (Data):**")
            st.json(block.data)
