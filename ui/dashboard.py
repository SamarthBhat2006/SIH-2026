"""
Dashboard View Module
Main workspace for source ingestion, security screening, configuration, multi-artefact generation, and export.
Styled with the Gumroad-inspired clean light design system.
"""

import time
import json
import streamlit as st
from pathlib import Path
from typing import Dict, List, Any

from config.settings import (
    AUDIENCE_OPTIONS,
    TONE_OPTIONS,
    DETAIL_LEVEL_OPTIONS,
    OBJECTIVE_OPTIONS,
    OUTPUT_TYPES,
    SAMPLE_DATA_DIR
)
from modules.document_processor import DocumentProcessor, DocumentProcessingError
from modules.security import SecurityScanner
from modules.hashing import IntegrityHasher
from modules.blockchain import BlockchainLedger
from modules.history import TransformationHistoryDB
from modules.ai_engine import AIEngine
from ui.components import (
    render_pipeline_stepper,
    render_security_badges,
    render_hash_badge,
    render_interactive_slide_deck
)

def render_dashboard(ledger: BlockchainLedger, history_db: TransformationHistoryDB) -> None:
    """Renders the main Content Transformation Dashboard."""

    # Initialize Session State Variables
    if "source_content" not in st.session_state:
        st.session_state.source_content = ""
    if "source_name" not in st.session_state:
        st.session_state.source_name = "Direct_Text_Input.txt"
    if "source_type" not in st.session_state:
        st.session_state.source_type = "text"
    if "security_report" not in st.session_state:
        st.session_state.security_report = None
    if "source_hash" not in st.session_state:
        st.session_state.source_hash = ""
    if "transformation_results" not in st.session_state:
        st.session_state.transformation_results = None
    if "output_hashes" not in st.session_state:
        st.session_state.output_hashes = {}
    if "last_block" not in st.session_state:
        st.session_state.last_block = None
    if "pipeline_stage" not in st.session_state:
        st.session_state.pipeline_stage = 0

    # Layout: Top Quick Actions
    col_demo, col_clear = st.columns([3.5, 1])
    with col_demo:
        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("📁 Load Incident Report (Demo 1)", use_container_width=True):
                sample_file = SAMPLE_DATA_DIR / "incident_report.txt"
                if sample_file.exists():
                    text = sample_file.read_text(encoding="utf-8")
                    st.session_state.source_content = text
                    st.session_state.source_name = "Incident_Response_Report_IR2026.txt"
                    st.session_state.source_type = "txt"
                    st.session_state.security_report = SecurityScanner.full_scan(text)
                    st.session_state.source_hash = IntegrityHasher.hash_text(text)
                    st.session_state.transformation_results = None
                    st.session_state.pipeline_stage = 2
                    st.rerun()
        with c2:
            if st.button("🛡️ Load Threat Advisory (Demo 2)", use_container_width=True):
                sample_file = SAMPLE_DATA_DIR / "threat_advisory.txt"
                if sample_file.exists():
                    text = sample_file.read_text(encoding="utf-8")
                    st.session_state.source_content = text
                    st.session_state.source_name = "Threat_Advisory_VPN_ZeroDay.txt"
                    st.session_state.source_type = "txt"
                    st.session_state.security_report = SecurityScanner.full_scan(text)
                    st.session_state.source_hash = IntegrityHasher.hash_text(text)
                    st.session_state.transformation_results = None
                    st.session_state.pipeline_stage = 2
                    st.rerun()

    with col_clear:
        if st.button("Clear", use_container_width=True):
            st.session_state.source_content = ""
            st.session_state.source_name = "Direct_Text_Input.txt"
            st.session_state.source_type = "text"
            st.session_state.security_report = None
            st.session_state.source_hash = ""
            st.session_state.transformation_results = None
            st.session_state.output_hashes = {}
            st.session_state.pipeline_stage = 0
            st.rerun()

    # Transformation Pipeline Visualizer
    render_pipeline_stepper(st.session_state.pipeline_stage)

    # Main Grid: Left = Input & Config, Right = Results & Artefacts
    col_left, col_right = st.columns([1, 1], gap="large")

    # ==========================================
    # LEFT COLUMN: SOURCE INGESTION & CONFIG
    # ==========================================
    with col_left:
        st.markdown("""
        <div class="paper-card">
            <div class="paper-card-title">📥 1. Source Document Ingestion</div>
        """, unsafe_allow_html=True)

        input_method = st.radio(
            "Ingestion Method:",
            ["Direct Paste", "Upload Document (PDF, DOCX, TXT)"],
            horizontal=True
        )

        if input_method == "Direct Paste":
            pasted_text = st.text_area(
                "Source Content / Briefing:",
                value=st.session_state.source_content,
                height=170,
                placeholder="Paste raw cybersecurity incident logs, operational briefings, intelligence notes, or policy documents..."
            )
            if pasted_text != st.session_state.source_content:
                st.session_state.source_content = pasted_text
                st.session_state.source_name = "Pasted_Operational_Brief.txt"
                st.session_state.source_type = "text"
                if pasted_text.strip():
                    st.session_state.security_report = SecurityScanner.full_scan(pasted_text)
                    st.session_state.source_hash = IntegrityHasher.hash_text(pasted_text)
                    st.session_state.pipeline_stage = 2
                else:
                    st.session_state.security_report = None
                    st.session_state.source_hash = ""
                    st.session_state.pipeline_stage = 0

        else:
            uploaded_file = st.file_uploader(
                "Choose file:",
                type=["txt", "pdf", "docx"],
                help="Max size 10MB"
            )
            if uploaded_file is not None:
                try:
                    bytes_data = uploaded_file.read()
                    parsed = DocumentProcessor.process_upload(uploaded_file.name, bytes_data)
                    st.session_state.source_content = parsed["content"]
                    st.session_state.source_name = parsed["file_name"]
                    st.session_state.source_type = parsed["source_type"]
                    st.session_state.security_report = SecurityScanner.full_scan(parsed["content"])
                    st.session_state.source_hash = IntegrityHasher.hash_text(parsed["content"])
                    st.session_state.pipeline_stage = 2
                    st.success(f"✓ Extracted {parsed['word_count']} words from {uploaded_file.name}")
                except DocumentProcessingError as e:
                    st.error(f"Extraction Error: {str(e)}")

        # Source Metadata & Security Panel
        if st.session_state.source_content:
            st.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1.25rem 0;'>", unsafe_allow_html=True)
            render_hash_badge(st.session_state.source_hash, "Source Hash")
            
            if st.session_state.security_report:
                render_security_badges(st.session_state.security_report)

        st.markdown("</div>", unsafe_allow_html=True)

        # Configuration Section
        st.markdown("""
        <div class="paper-card">
            <div class="paper-card-title">⚙️ 2. Transformation Settings</div>
        """, unsafe_allow_html=True)

        cfg_col1, cfg_col2 = st.columns(2)
        with cfg_col1:
            selected_audience = st.selectbox("Target Audience:", AUDIENCE_OPTIONS, index=0)
            selected_detail = st.selectbox("Level of Detail:", DETAIL_LEVEL_OPTIONS, index=1)
        with cfg_col2:
            selected_tone = st.selectbox("Tone:", TONE_OPTIONS, index=0)
            selected_objective = st.selectbox("Objective:", OBJECTIVE_OPTIONS, index=0)

        # Target Output Formats
        st.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1rem 0;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-weight:600; font-size:0.9rem; color:#000000; margin-bottom: 0.5rem;'>3. Target Formats (Multi-Artefact)</div>", unsafe_allow_html=True)

        c_opt1, c_opt2 = st.columns(2)
        with c_opt1:
            chk_exec = st.checkbox("Executive Summary", value=True)
            chk_adv = st.checkbox("Cybersecurity Advisory", value=True)
            chk_pres = st.checkbox("Presentation Deck", value=True)
        with c_opt2:
            chk_link = st.checkbox("LinkedIn Post", value=True)
            chk_x = st.checkbox("X / Twitter Thread", value=True)

        selected_outputs = []
        if chk_exec: selected_outputs.append("executive_summary")
        if chk_adv: selected_outputs.append("cybersecurity_advisory")
        if chk_link: selected_outputs.append("linkedin_post")
        if chk_x: selected_outputs.append("x_thread")
        if chk_pres: selected_outputs.append("presentation")

        # Generate Button
        st.markdown("<br>", unsafe_allow_html=True)
        btn_transform = st.button(
            "Transform Content →",
            type="primary",
            use_container_width=True,
            disabled=not (st.session_state.source_content.strip() and selected_outputs)
        )

        st.markdown("</div>", unsafe_allow_html=True)

        if btn_transform:
            if not st.session_state.source_content.strip():
                st.warning("Please provide source content first.")
            elif not selected_outputs:
                st.warning("Please select at least one target format.")
            else:
                config_meta = {
                    "audience": selected_audience,
                    "tone": selected_tone,
                    "detail": selected_detail,
                    "objective": selected_objective
                }

                progress_bar = st.progress(0, text="Initiating Grounded Transformation...")
                
                # Step 1: Security Screening
                st.session_state.pipeline_stage = 2
                progress_bar.progress(25, text="Running Input Security Analysis...")
                time.sleep(0.3)
                
                # Step 2: Content Analysis & Grounding
                st.session_state.pipeline_stage = 3
                progress_bar.progress(50, text="Extracting Grounding Facts...")
                time.sleep(0.3)
                
                # Step 3: Multi-AI Transformation
                st.session_state.pipeline_stage = 4
                progress_bar.progress(70, text=f"Generating {len(selected_outputs)} Artefacts...")
                
                ai = AIEngine()
                results = ai.generate_multiple_artefacts(
                    selected_outputs,
                    st.session_state.source_content,
                    config_meta
                )
                
                # Step 4: Cryptographic Hashing
                st.session_state.pipeline_stage = 5
                progress_bar.progress(85, text="Generating SHA-256 Digests...")
                out_hashes = IntegrityHasher.generate_artefact_hashes(results)
                time.sleep(0.2)
                
                # Step 5: Mint Blockchain Block & Save History
                st.session_state.pipeline_stage = 6
                progress_bar.progress(95, text="Recording to Blockchain Ledger...")
                
                sec_stat = st.session_state.security_report.get("overall_status", "CLEAN") if st.session_state.security_report else "CLEAN"
                
                new_block = ledger.add_transformation_block(
                    transformation_id=f"DOC-{int(time.time()) % 100000:05d}",
                    source_name=st.session_state.source_name,
                    source_hash=st.session_state.source_hash,
                    output_hashes=out_hashes,
                    config_metadata=config_meta,
                    security_status=sec_stat
                )
                
                doc_id = history_db.save_transformation(
                    source_name=st.session_state.source_name,
                    source_type=st.session_state.source_type,
                    source_hash=st.session_state.source_hash,
                    source_content=st.session_state.source_content,
                    security_status=sec_stat,
                    security_report=st.session_state.security_report or {},
                    config=config_meta,
                    selected_outputs=selected_outputs,
                    outputs=results,
                    output_hashes=out_hashes,
                    block_index=new_block.index,
                    block_hash=new_block.hash
                )
                
                progress_bar.progress(100, text="Transformation Complete!")
                time.sleep(0.2)
                progress_bar.empty()

                st.session_state.transformation_results = results
                st.session_state.output_hashes = out_hashes
                st.session_state.last_block = new_block
                st.rerun()

    # ==========================================
    # RIGHT COLUMN: GENERATED ARTEFACTS
    # ==========================================
    with col_right:
        st.markdown("""
        <div class="paper-card">
            <div class="paper-card-title">📤 Generated Communication Artefacts</div>
        """, unsafe_allow_html=True)

        if not st.session_state.transformation_results:
            st.markdown("""
            <div style="text-align: center; padding: 3rem 1.5rem; color: #575756;">
                <div style="font-size: 2.2rem; margin-bottom: 0.6rem;">📄</div>
                <div style="font-weight: 700; color: #000000; font-size: 1.05rem; margin-bottom: 0.35rem;">
                    Ready for Generation
                </div>
                <div style="font-size: 0.88rem; max-width: 360px; margin: 0 auto; color: #575756;">
                    Ingest source content on the left, pick target parameters, and click 
                    <strong>Transform Content</strong> to generate all communication artefacts from 1 source.
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            results = st.session_state.transformation_results
            out_hashes = st.session_state.output_hashes
            block = st.session_state.last_block

            # Top Ledger Anchor Badge
            if block:
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0 1rem 0; border-bottom: 1px solid #d1d5dc; margin-bottom: 1rem;">
                    <span class="verified-pill">✓ Anchored in Block #{block.index}</span>
                    <span style="font-size: 0.78rem; color: #575756; font-family: monospace;">Prev: {block.previous_hash[:12]}...</span>
                </div>
                """, unsafe_allow_html=True)

            # Output Tabs
            tab_titles = [OUTPUT_TYPES.get(k, k.title()) for k in results.keys()]
            tabs = st.tabs(tab_titles)

            for i, (art_key, content) in enumerate(results.items()):
                with tabs[i]:
                    hash_val = out_hashes.get(art_key, "N/A")
                    render_hash_badge(hash_val, f"{OUTPUT_TYPES.get(art_key)} Hash")

                    col_c1, col_c2 = st.columns([1, 1])
                    with col_c1:
                        st.download_button(
                            label=f"Download (.md)",
                            data=content,
                            file_name=f"{art_key}_{int(time.time())}.md",
                            mime="text/markdown",
                            key=f"dl_{art_key}"
                        )
                    with col_c2:
                        st.download_button(
                            label=f"Download (.txt)",
                            data=content,
                            file_name=f"{art_key}_{int(time.time())}.txt",
                            mime="text/plain",
                            key=f"dl_txt_{art_key}"
                        )

                    st.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1rem 0;'>", unsafe_allow_html=True)

                    if art_key == "presentation":
                        render_interactive_slide_deck(content, key_suffix="dash")
                    else:
                        st.markdown(content)

            # Export Complete Transformation Package
            st.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1.25rem 0;'>", unsafe_allow_html=True)
            audit_bundle = {
                "source_name": st.session_state.source_name,
                "source_hash": st.session_state.source_hash,
                "artefact_hashes": out_hashes,
                "artefacts": results,
                "blockchain_block": block.to_dict() if block else None
            }
            st.download_button(
                label="📦 Download Complete Audit Package (.JSON)",
                data=json.dumps(audit_bundle, indent=2),
                file_name=f"transformation_audit_package_{int(time.time())}.json",
                mime="application/json",
                use_container_width=True
            )

        st.markdown("</div>", unsafe_allow_html=True)
