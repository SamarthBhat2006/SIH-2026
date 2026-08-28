"""
History & Audit Inspector View Module
Visualizes past transformation events, security statuses, cryptographic hashes, and stored artefacts.
Styled with the Gumroad-inspired clean light design system.
"""

import json
import streamlit as st
from modules.history import TransformationHistoryDB
from ui.components import render_hash_badge, render_interactive_slide_deck

def render_history_view(history_db: TransformationHistoryDB) -> None:
    """Renders the historical transformation audit log."""
    st.markdown("### 📜 Transformation Audit & History")
    st.caption("Immutable record of all source documents and derived communication artefacts.")

    records = history_db.get_all(limit=50)

    if not records:
        st.markdown("""
        <div class="paper-card" style="text-align: center; padding: 2.5rem; color: #575756;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📂</div>
            <div style="font-weight: 700; color: #000000;">No Transformation History Found</div>
            <div style="font-size: 0.88rem; margin-top: 0.25rem;">Transform a document in the Dashboard to record your first cryptographic audit log.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Metrics Summary
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{len(records)}</div>
            <div class="metric-title">Total Transformations</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        verified_count = sum(1 for r in records if r["block_index"] is not None)
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{verified_count}</div>
            <div class="metric-title">Anchored Blocks</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        clean_count = sum(1 for r in records if "WARNING" not in r["security_status"])
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{clean_count}</div>
            <div class="metric-title">Clean Security Scans</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Search & Filter
    search_term = st.text_input("🔍 Search History by Document ID or File Name:", placeholder="e.g. DOC- or Incident_Report...")

    filtered_records = records
    if search_term.strip():
        term = search_term.strip().lower()
        filtered_records = [
            r for r in records 
            if term in r["id"].lower() or term in r["source_name"].lower()
        ]

    # Render Record Cards / Accordions
    for rec in filtered_records:
        sec_label = "Clean" if "CLEAN" in rec["security_status"] else ("Notice" if "NOTICE" in rec["security_status"] else "Warning")
        
        with st.expander(f"📄 {rec['id']} — {rec['source_name']} ({rec['created_at_str']}) — Block #{rec['block_index']}"):
            c1, c2 = st.columns([1, 1])
            with c1:
                st.markdown(f"**Document ID:** `{rec['id']}`")
                st.markdown(f"**Source Format:** `{rec['source_type'].upper()}`")
                st.markdown(f"**Security Scan:** `{sec_label}`")
                render_hash_badge(rec['source_hash'], "Source Hash")
            with c2:
                st.markdown(f"**Anchored Block:** `#{rec['block_index']}`")
                st.markdown(f"**Block Hash:** `{rec['block_hash'][:18]}...`")
                st.markdown(f"**Artefacts Generated:** `{len(rec['selected_outputs'])} outputs`")
                st.markdown(f"**Settings:** *Audience:* {rec['config'].get('audience')} | *Tone:* {rec['config'].get('tone')}")

            st.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1rem 0;'>", unsafe_allow_html=True)
            st.markdown("#### Generated Artefacts")

            sub_tabs = st.tabs([k.replace("_", " ").title() for k in rec["outputs"].keys()])
            for idx, (art_name, art_content) in enumerate(rec["outputs"].items()):
                with sub_tabs[idx]:
                    art_hash = rec["output_hashes"].get(art_name, "N/A")
                    render_hash_badge(art_hash, f"{art_name.title()} Hash")
                    if art_name == "presentation":
                        render_interactive_slide_deck(art_content, key_suffix=f"hist_{rec['id']}")
                    else:
                        st.markdown(art_content)
