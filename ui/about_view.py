"""
About & System Documentation View Module
Details problem statement 26154, system architecture, security compliance, and research provenance.
Styled with the Gumroad-inspired clean light design system.
"""

import streamlit as st

def render_about_view() -> None:
    """Renders the About and Problem Statement Documentation."""
    st.markdown("### 🏛️ National Technical Research Organisation (NTRO)")
    st.markdown("#### Problem Statement ID: 26154 — Gen AI Platform for Automated Content Transformation")
    st.caption("Theme: Blockchain & Cybersecurity | Category: Software")

    st.markdown("""
    <div class="gumroad-box">
        <div class="gumroad-box-title">🎯 The Core Challenge</div>
        <p style="color: var(--color-graphite); font-size: 0.92rem; line-height: 1.6; margin: 0;">
            Government and national technical organizations process massive volumes of operational documents daily: 
            cyber threat advisories, technical post-mortems, and regulatory directives. Disseminating this single source of truth 
            across diverse audiences (Leadership, Technical Teams, Partner Agencies, and the Public) requires rapid, grounded, 
            and cryptographically auditable multi-artefact transformation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="gumroad-box">
            <div class="gumroad-box-title">🛡️ Security & Zero-Trust Defense</div>
            <ul style="color: var(--color-graphite); font-size: 0.88rem; line-height: 1.6; padding-left: 1.2rem; margin: 0;">
                <li><strong>Untrusted Data Isolation:</strong> Ingested content is treated strictly as passive data.</li>
                <li><strong>Adversarial Injection Scanner:</strong> Catches prompt overrides, jailbreaks, and system hijacking.</li>
                <li><strong>Sensitive Pattern Identifier:</strong> Scans for exposed internal IPv4/IPv6, API keys, and credentials.</li>
                <li><strong>Grounded Anti-Hallucination:</strong> Deterministic extraction ensures the AI never invents facts or IoCs.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="gumroad-box">
            <div class="gumroad-box-title">⛓️ Cryptographic Provenance & Ledger</div>
            <ul style="color: var(--color-graphite); font-size: 0.88rem; line-height: 1.6; padding-left: 1.2rem; margin: 0;">
                <li><strong>SHA-256 Digital Fingerprints:</strong> Deterministic hashing for original source and all artefacts.</li>
                <li><strong>Append-Only Blockchain Ledger:</strong> Sequential blocks linked by cryptographic hashes.</li>
                <li><strong>Real-Time Tamper Detection:</strong> Validates ledger integrity and pinpoints any corrupted block.</li>
                <li><strong>Zero Secret Leakage:</strong> Strict environment variables with offline fallback reliability.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border:0; border-top:1px solid var(--color-hairline); margin: 1.5rem 0;'>", unsafe_allow_html=True)
    st.markdown("### 📊 Architecture & Transformation Workflow")
    
    st.markdown("""
    ```text
    ┌──────────────────────────┐
    │  Trusted Source Input    │ (Direct Paste / TXT / PDF / DOCX)
    └─────────────┬────────────┘
                  ▼
    ┌──────────────────────────┐
    │  Security & Threat Scan  │ (Prompt Injection Check + Sensitive Data Scan)
    └─────────────┬────────────┘
                  ▼
    ┌──────────────────────────┐
    │  Grounded Fact Extractor │ (Anti-Hallucination Structure: IoCs, CVEs, Dates)
    └─────────────┬────────────┘
                  ▼
    ┌──────────────────────────┐
    │  Unified AI Engine       │ (Gemini / OpenAI / Grounded Fallback Engine)
    └─────────────┬────────────┘
                  ▼
    ┌──────────────────────────┐
    │  Multi-Artefact Outputs  │ (Exec Summary, Advisory, LinkedIn, X Thread, Deck)
    └─────────────┬────────────┘
                  ▼
    ┌──────────────────────────┐
    │  SHA-256 Cryptography    │ (Source Hash + Individual Output Hashes)
    └─────────────┬────────────┘
                  ▼
    ┌──────────────────────────┐
    │  Blockchain Audit Ledger │ (Chained Blocks + SQLite Historical Persistence)
    └──────────────────────────┘
    ```
    """)
