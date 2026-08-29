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
    """Renders the top navbar with brand, theme toggle button, and NTRO Core badge."""
    col_brand, col_spacer, col_actions = st.columns([3.5, 3.5, 3.0])

    with col_brand:
        st.markdown("""
        <div class="gumroad-brand-group" style="padding-top: 4px;">
            <span class="gumroad-logo">⚡ transform</span>
        </div>
        """, unsafe_allow_html=True)

    with col_actions:
        c_theme, c_badge = st.columns([1.4, 1.1])
        with c_theme:
            current_theme = st.session_state.get("theme", "light")
            theme_btn_label = "🌙 Dark Mode" if current_theme == "light" else "☀️ Light Mode"
            if st.button(theme_btn_label, key="btn_theme_toggle", use_container_width=True):
                st.session_state.theme = "dark" if current_theme == "light" else "light"
                st.rerun()

        with c_badge:
            st.markdown("""
            <div style="text-align: right; padding-top: 3px;">
                <span class="ntro-core-badge" style="font-size: 0.82rem; font-weight: 700; color: #000000; padding: 6px 14px; background-color: #ff90e8; border: 1.5px solid #000000; border-radius: 9999px; display: inline-block;">NTRO Core</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr style='border:0; border-top:1px solid var(--color-hairline); margin: 0.75rem 0 1.75rem 0;'>", unsafe_allow_html=True)

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
<p style="font-size:18px;line-height:1.56;letter-spacing:-0.108px;color:#242423;text-align:center;width:100%;max-width:720px;margin:0 auto 20px auto;display:block;">Transform raw operational briefs and cyber reports into grounded executive summaries, advisories, social threads, and presentations with cryptographic proof.</p>
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
<div style="font-size: 0.88rem; color: var(--color-graphite); margin-bottom: 0.35rem;">Adversarial instructions flagged in source text: <strong>{matched_preview}</strong></div>
<div style="font-size: 0.82rem; color: var(--color-muted, #a1a1aa);">{inj.get('mitigation_note')}</div>
</div>"""
        st.markdown(html, unsafe_allow_html=True)

    if sens.get("has_sensitive_data"):
        findings = sens.get("findings_by_category", {})
        categories = list(findings.keys())
        html = f"""<div class="alert-yellow-box">
<div style="font-weight: 800; color: #d97706; font-size: 0.95rem; margin-bottom: 0.3rem;">🔍 Sensitive Information Patterns Detected ({sens.get('total_sensitive_items')} Matches)</div>
<div style="font-size: 0.88rem; color: var(--color-graphite); margin-bottom: 0.35rem;">Detected patterns: <strong>{', '.join(categories)}</strong></div>
<div style="font-size: 0.82rem; color: var(--color-muted, #a1a1aa);">{sens.get('advisory_note')}</div>
</div>"""
        st.markdown(html, unsafe_allow_html=True)

def render_hash_badge(hash_val: str, label: str = "SHA-256 Digest") -> None:
    """Renders a formatted cryptographic hash badge."""
    html = f"""<div style="margin: 0.4rem 0;">
<span style="font-size: 0.8rem; color: var(--color-graphite); font-weight: 700;">{label}: </span>
<span class="gumroad-hash">{hash_val}</span>
</div>"""
    st.markdown(html, unsafe_allow_html=True)

def parse_slides_markdown(content: str) -> List[Dict[str, Any]]:
    """Parses markdown generated for slides into structured slide objects."""
    slide_blocks = re.split(r"(?:^|\n)---+(?:\n|$)|(?:^|\n)##\s+SLIDE\s+\d+[\s:—–-]+", content)
    slides = []
    
    for block in slide_blocks:
        block = block.strip()
        if not block:
            continue
            
        lines = block.split("\n")
        title = "Executive Briefing"
        body_lines = []
        notes = "Deliver key operational insights clearly and concisely."
        
        in_notes = False
        notes_lines = []
        
        for line in lines:
            if "speaker notes:" in line.lower() or "presenter notes:" in line.lower() or "**speaker notes:**" in line.lower() or "**presenter notes:**" in line.lower():
                in_notes = True
                continue
                
            if in_notes:
                notes_lines.append(line)
            else:
                if line.startswith("#"):
                    title = line.lstrip("#").strip()
                elif line.startswith("**Title:**") or line.startswith("Title:"):
                    title = line.replace("**Title:**", "").replace("Title:", "").strip()
                else:
                    body_lines.append(line)
                    
        if notes_lines:
            notes = "\n".join(notes_lines).strip()
            
        body = "\n".join(body_lines).strip()
        slides.append({
            "title": title,
            "body": body,
            "notes": notes
        })
        
    return slides if slides else [{"title": "Presentation Overview", "body": content, "notes": "Standard briefing notes."}]

def render_interactive_slide_deck(slides_content: str, key_suffix: str = "main") -> None:
    """Renders an interactive pagination-based slide deck carousel."""
    slides = parse_slides_markdown(slides_content)
    total_slides = len(slides)
    
    state_key = f"current_slide_{key_suffix}"
    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    current_idx = min(st.session_state[state_key], total_slides - 1)

    col_prev, col_num, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("← Previous", key=f"prev_{key_suffix}", disabled=(current_idx == 0)):
            st.session_state[state_key] = max(0, current_idx - 1)
            st.rerun()
            
    with col_num:
        st.markdown(f"<div style='text-align: center; font-weight: 800; color: var(--color-ink-black); padding-top: 8px; font-size: 0.92rem;'>SLIDE {current_idx + 1} OF {total_slides}</div>", unsafe_allow_html=True)
        
    with col_next:
        if st.button("Next →", key=f"next_{key_suffix}", disabled=(current_idx == total_slides - 1)):
            st.session_state[state_key] = min(total_slides - 1, current_idx + 1)
            st.rerun()

    slide = slides[current_idx]
    st.markdown(f"""<div class="slide-deck-box">
<div class="slide-deck-title">📄 {slide['title']}</div>
<div style="font-size: 0.98rem; color: var(--color-graphite); line-height: 1.65;">
""", unsafe_allow_html=True)
    
    st.markdown(slide['body'])
    
    st.markdown(f"""</div>
<div class="slide-deck-notes">
<strong style="color: var(--color-ink-black); font-weight: 800;">🎙️ Presenter Notes:</strong><br>
{slide['notes']}
</div>
</div>""", unsafe_allow_html=True)
