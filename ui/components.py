"""
UI Components Module
Reusable visual widgets, cards, presentation viewers, and pipeline visualizers.
"""

import re
import json
import streamlit as st
from typing import Dict, List, Any, Optional

def render_header() -> None:
    """Renders the top branding banner."""
    st.markdown("""
    <div class="ntro-header-container">
        <div>
            <h1 class="ntro-title">⚡ NTRO GEN AI CONTENT TRANSFORMATION</h1>
            <div class="ntro-subtitle">Problem Statement #26154 | Multi-Artefact Transformation • Cryptographic Ledger • Grounded Intelligence</div>
        </div>
        <div>
            <span class="ntro-badge">🛡️ NTRO CYBER ENGINE v1.0</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_pipeline_stepper(current_stage: int = 0) -> None:
    """
    Renders the 6-stage transformation pipeline visualizer.
    Stages:
    0: Idle
    1: Ingestion & Extraction
    2: Security Screening
    3: Grounded Analysis
    4: Multi-AI Transformation
    5: SHA-256 Hashing
    6: Blockchain Ledger Minted
    """
    stages = [
        {"num": "1", "name": "Source Ingest", "icon": "📄"},
        {"num": "2", "name": "Security Scan", "icon": "🛡️"},
        {"num": "3", "name": "Fact Grounding", "icon": "🔍"},
        {"num": "4", "name": "AI Transform", "icon": "⚡"},
        {"num": "5", "name": "SHA-256 Hash", "icon": "🔐"},
        {"num": "6", "name": "Block Ledger", "icon": "⛓️"},
    ]

    html = '<div class="pipeline-container">'
    for i, stage in enumerate(stages, 1):
        if i < current_stage:
            cls = "step-complete"
            icon = "✓"
        elif i == current_stage:
            cls = "step-active"
            icon = stage["icon"]
        else:
            cls = "step-idle"
            icon = stage["icon"]

        html += f"""
        <div class="pipeline-step {cls}">
            <div class="pipeline-icon">{icon}</div>
            <div class="pipeline-label">{stage['name']}</div>
        </div>
        """
        if i < len(stages):
            html += '<div class="pipeline-arrow">➔</div>'

    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def render_security_badges(security_report: Dict[str, Any]) -> None:
    """Renders security and sensitive data alerts."""
    inj = security_report.get("injection_report", {})
    sens = security_report.get("sensitive_report", {})

    if inj.get("has_injection_risk"):
        sigs = inj.get("signatures", [])
        matched_preview = ", ".join([f"'{s['matched_text']}'" for s in sigs[:3]])
        st.markdown(f"""
        <div class="sec-warning-card">
            <div class="sec-warning-title">⚠️ POTENTIAL PROMPT INJECTION DETECTED ({inj.get('risk_level')} RISK)</div>
            <div style="font-size: 0.85rem; color: #ff8a80; margin-bottom: 0.3rem;">
                Adversarial instructions identified in source text: {matched_preview}
            </div>
            <div style="font-size: 0.78rem; color: #b0bec5;">
                {inj.get('mitigation_note')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    if sens.get("has_sensitive_data"):
        findings = sens.get("findings_by_category", {})
        categories = list(findings.keys())
        st.markdown(f"""
        <div class="sec-notice-card">
            <div class="sec-notice-title">🔍 SENSITIVE INFORMATION DETECTED ({sens.get('total_sensitive_items')} Items)</div>
            <div style="font-size: 0.85rem; color: #ffe082; margin-bottom: 0.3rem;">
                Pattern Matches: <strong>{', '.join(categories)}</strong>
            </div>
            <div style="font-size: 0.78rem; color: #cfd8dc;">
                {sens.get('advisory_note')}
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_hash_badge(hash_val: str, label: str = "SHA-256 Digest") -> None:
    """Renders a formatted cryptographic hash badge."""
    st.markdown(f"""
    <div style="margin: 0.4rem 0;">
        <span style="font-size: 0.75rem; color: #8b949e; text-transform: uppercase; font-weight: 600;">{label}: </span>
        <span class="hash-chip">{hash_val}</span>
    </div>
    """, unsafe_allow_html=True)

def parse_slides_markdown(content: str) -> List[Dict[str, Any]]:
    """Parses markdown generated for slides into structured slide objects."""
    slide_blocks = re.split(r"(?:^|\n)---+(?:\n|$)|(?:^|\n)##\s+SLIDE\s+\d+:\s*", content)
    slides = []
    
    for block in slide_blocks:
        clean = block.strip()
        if not clean:
            continue
            
        lines = clean.split("\n")
        title = lines[0].replace("##", "").replace("SLIDE", "").strip()
        if title.startswith(":") or title.startswith("-"):
            title = title[1:].strip()
        if not title:
            title = "Presentation Slide"

        # Separate speaker notes
        notes = "No speaker notes provided."
        body_lines = []
        in_notes = False
        notes_lines = []
        
        for line in lines[1:]:
            if "speaker notes:" in line.lower() or "**speaker notes:**" in line.lower():
                in_notes = True
                continue
            if in_notes:
                notes_lines.append(line)
            else:
                body_lines.append(line)
                
        if notes_lines:
            notes = "\n".join(notes_lines).strip()
            
        slides.append({
            "title": title,
            "body": "\n".join(body_lines).strip(),
            "notes": notes
        })

    if not slides:
        slides = [{
            "title": "Presentation Overview",
            "body": content,
            "notes": "Generated directly from source."
        }]
    return slides

def render_interactive_slide_deck(presentation_text: str, key_suffix: str = "deck") -> None:
    """Renders an interactive slide-by-slide presentation deck viewer."""
    slides = parse_slides_markdown(presentation_text)
    total_slides = len(slides)
    
    state_key = f"slide_idx_{key_suffix}"
    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    current_idx = min(st.session_state[state_key], total_slides - 1)

    # Deck Header Controls
    col_prev, col_num, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("◀ Previous Slide", key=f"prev_{key_suffix}", disabled=(current_idx == 0)):
            st.session_state[state_key] = max(0, current_idx - 1)
            st.rerun()
            
    with col_num:
        st.markdown(f"<div style='text-align: center; font-weight: 700; color: #00e5ff; padding-top: 5px;'>SLIDE {current_idx + 1} OF {total_slides}</div>", unsafe_allow_html=True)
        
    with col_next:
        if st.button("Next Slide ▶", key=f"next_{key_suffix}", disabled=(current_idx == total_slides - 1)):
            st.session_state[state_key] = min(total_slides - 1, current_idx + 1)
            st.rerun()

    # Active Slide Render
    slide = slides[current_idx]
    st.markdown(f"""
    <div class="slide-card">
        <div class="slide-title">📌 {slide['title']}</div>
        <div style="font-size: 0.95rem; color: #e6edf3; line-height: 1.6;">
    """, unsafe_allow_html=True)
    
    st.markdown(slide['body'])
    
    st.markdown(f"""
        </div>
        <div class="speaker-notes-box">
            <strong style="color: #58a6ff;">🎙️ Presenter Notes:</strong><br>
            {slide['notes']}
        </div>
    </div>
    """, unsafe_allow_html=True)
