"""
UI Components Module
Renders authentic Gumroad UI elements customized for the NTRO Transformation Platform:
- Top Navigation Bar with Logo, Stat Badge, Nav links, and Action Button.
- Hero Banner with oversized typography and project-themed sticker badges.
- Pipeline stepper, security alerts, and slide deck viewer.
"""

import re
import json
import streamlit as st
from typing import Dict, List, Any, Optional

def render_top_navbar(current_view: str = "Dashboard") -> None:
    """Renders the exact Gumroad top navigation bar."""
    html = f"""<div class="gumroad-nav-wrapper">
<div class="gumroad-brand-group">
<span class="gumroad-logo">transform</span>
<span class="gumroad-stat-pill">⚡ 26154 ★</span>
</div>
<div class="gumroad-nav-links">
<span class="{'nav-pill-active' if current_view == 'Dashboard' else 'nav-link-item'}">Dashboard</span>
<span class="{'nav-pill-active' if current_view == 'History' else 'nav-link-item'}">History</span>
<span class="{'nav-pill-active' if current_view == 'Ledger' else 'nav-link-item'}">Ledger</span>
<span class="{'nav-pill-active' if current_view == 'About' else 'nav-link-item'}">About</span>
</div>
<div>
<span style="font-size: 0.88rem; font-weight: 700; color: #000000; padding: 7px 18px; background-color: #ff90e8; border: 1.5px solid #000000; border-radius: 9999px;">NTRO Core</span>
</div>
</div>"""
    st.markdown(html, unsafe_allow_html=True)

def render_hero_banner() -> None:
    """Renders the clean Gumroad hero banner with project-relevant sticker badges."""
    html = """<div class="gumroad-hero-container">
<div class="hero-stickers-row">
<span class="project-sticker sticker-pink">⚡ AI Transformation Engine</span>
<span class="project-sticker sticker-yellow">🛡️ Threat Screening</span>
<span class="project-sticker sticker-white">🔐 SHA-256 Hashing</span>
<span class="project-sticker sticker-lime">⛓️ Blockchain Ledger</span>
</div>
<h1 class="gumroad-hero-h1">1 Source to 5 Artefacts</h1>
<p class="gumroad-hero-sub">Transform raw operational briefs and cyber reports into grounded executive summaries, advisories, social threads, and presentations with cryptographic proof.</p>
<div class="artefact-pills-row">
<span class="artefact-pill">📋 Executive Summary</span>
<span class="artefact-pill">🚨 Cybersecurity Advisory</span>
<span class="artefact-pill">💼 LinkedIn Post</span>
<span class="artefact-pill">🧵 X Thread</span>
<span class="artefact-pill">📊 Presentation Deck</span>
</div>
</div>"""
    st.markdown(html, unsafe_allow_html=True)

def render_pipeline_stepper(current_stage: int = 0) -> None:
    """Renders the 6-stage transformation pipeline stepper."""
    stages = [
        {"num": "1", "name": "Source Ingest"},
        {"num": "2", "name": "Security Scan"},
        {"num": "3", "name": "Fact Grounding"},
        {"num": "4", "name": "AI Transform"},
        {"num": "5", "name": "SHA-256 Hash"},
        {"num": "6", "name": "Block Ledger"},
    ]

    html = '<div class="gumroad-stepper-bar">'
    for i, stage in enumerate(stages, 1):
        if i < current_stage:
            cls = "done"
            icon = "✓"
        elif i == current_stage:
            cls = "active"
            icon = stage["num"]
        else:
            cls = "idle"
            icon = stage["num"]

        html += f'<div class="step-item {cls}"><div class="step-bubble">{icon}</div><div class="step-text">{stage["name"]}</div></div>'
        if i < len(stages):
            html += '<div class="step-arrow">→</div>'

    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def render_security_badges(security_report: Dict[str, Any]) -> None:
    """Renders clean security notice cards with Gumroad accent styling."""
    inj = security_report.get("injection_report", {})
    sens = security_report.get("sensitive_report", {})

    if inj.get("has_injection_risk"):
        sigs = inj.get("signatures", [])
        matched_preview = ", ".join([f"'{s['matched_text']}'" for s in sigs[:3]])
        html = f"""<div class="alert-vermillion-box">
<div style="font-weight: 800; color: #dc341e; font-size: 0.95rem; margin-bottom: 0.3rem;">⚠️ Potential Prompt Injection Detected ({inj.get('risk_level')} Risk)</div>
<div style="font-size: 0.88rem; color: #242423; margin-bottom: 0.35rem;">Adversarial instructions flagged in source text: <strong>{matched_preview}</strong></div>
<div style="font-size: 0.82rem; color: #575756;">{inj.get('mitigation_note')}</div>
</div>"""
        st.markdown(html, unsafe_allow_html=True)

    if sens.get("has_sensitive_data"):
        findings = sens.get("findings_by_category", {})
        categories = list(findings.keys())
        html = f"""<div class="alert-yellow-box">
<div style="font-weight: 800; color: #946c00; font-size: 0.95rem; margin-bottom: 0.3rem;">🔍 Sensitive Information Patterns Detected ({sens.get('total_sensitive_items')} Matches)</div>
<div style="font-size: 0.88rem; color: #242423; margin-bottom: 0.35rem;">Detected patterns: <strong>{', '.join(categories)}</strong></div>
<div style="font-size: 0.82rem; color: #575756;">{sens.get('advisory_note')}</div>
</div>"""
        st.markdown(html, unsafe_allow_html=True)

def render_hash_badge(hash_val: str, label: str = "SHA-256 Digest") -> None:
    """Renders a formatted cryptographic hash badge."""
    html = f"""<div style="margin: 0.4rem 0;">
<span style="font-size: 0.8rem; color: #242423; font-weight: 700;">{label}: </span>
<span class="gumroad-hash">{hash_val}</span>
</div>"""
    st.markdown(html, unsafe_allow_html=True)

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

    col_prev, col_num, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("← Previous", key=f"prev_{key_suffix}", disabled=(current_idx == 0)):
            st.session_state[state_key] = max(0, current_idx - 1)
            st.rerun()
            
    with col_num:
        st.markdown(f"<div style='text-align: center; font-weight: 800; color: #000000; padding-top: 8px; font-size: 0.92rem;'>SLIDE {current_idx + 1} OF {total_slides}</div>", unsafe_allow_html=True)
        
    with col_next:
        if st.button("Next →", key=f"next_{key_suffix}", disabled=(current_idx == total_slides - 1)):
            st.session_state[state_key] = min(total_slides - 1, current_idx + 1)
            st.rerun()

    slide = slides[current_idx]
    st.markdown(f"""<div class="slide-deck-box">
<div class="slide-deck-title">📄 {slide['title']}</div>
<div style="font-size: 0.98rem; color: #242423; line-height: 1.65;">
""", unsafe_allow_html=True)
    
    st.markdown(slide['body'])
    
    st.markdown(f"""</div>
<div class="slide-deck-notes">
<strong style="color: #000000; font-weight: 800;">🎙️ Presenter Notes:</strong><br>
{slide['notes']}
</div>
</div>""", unsafe_allow_html=True)
