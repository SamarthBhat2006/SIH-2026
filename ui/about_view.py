"""
About & System Documentation View Module
Details problem statement 26154, system architecture, security compliance, and research provenance.
"""

import streamlit as st

def render_about_view() -> None:
    """Renders the About and Problem Statement Documentation."""
    st.markdown("### 🏛️ National Technical Research Organisation (NTRO)")
    st.markdown("#### Problem Statement ID: 26154 — Gen AI Platform for Automated Content Transformation")
    st.caption("Theme: Blockchain & Cybersecurity | Category: Software")

    st.markdown("""
    <div class="cyber-card">
        <div class="cyber-card-title">🎯 The Core Challenge</div>
        <p style="color: #c9d1d9; font-size: 0.92rem; line-height: 1.6;">
            Government and national intelligence bodies like the <strong>National Technical Research Organisation (NTRO)</strong> 
            process massive volumes of high-stakes information daily: cyber threat advisories, technical incident post-mortems, 
            satellite intelligence analyses, and regulatory directives. Disseminating this single source of truth across diverse audiences 
            (Cabinet Leadership, Technical SOC Engineers, Inter-Agency Partners, and Public Media) currently demands hours of manual, error-prone authoring.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="cyber-card">
            <div class="cyber-card-title">🛡️ Security & Zero-Trust Defense</div>
            <ul style="color: #c9d1d9; font-size: 0.88rem; line-height: 1.6; padding-left: 1.2rem;">
                <li><strong>Untrusted Data Isolation:</strong> Ingested text and documents are wrapped in passive token contexts.</li>
                <li><strong>Adversarial Injection Scanner:</strong> Heuristically catches prompt overrides, jailbreaks, and system hijacking.</li>
                <li><strong>Sensitive Pattern Identifier:</strong> Scans for exposed internal IPv4/IPv6, API keys, credentials, and emails.</li>
                <li><strong>Grounded Anti-Hallucination:</strong> Enforces deterministic extraction so the AI never fabricates IoCs, CVEs, or dates.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cyber-card">
            <div class="cyber-card-title">⛓️ Cryptographic Provenance & Ledger</div>
            <ul style="color: #c9d1d9; font-size: 0.88rem; line-height: 1.6; padding-left: 1.2rem;">
                <li><strong>SHA-256 Digital Fingerprints:</strong> Deterministic hashing for original source and every generated artefact.</li>
                <li><strong>Append-Only Blockchain Ledger:</strong> Sequential blocks linked by previous hash hashes for immutable auditability.</li>
                <li><strong>Real-Time Tamper Detection:</strong> Instant mathematical verification that alerts if any historical block has been altered.</li>
                <li><strong>Zero Secret Leakage:</strong> Strict environment configuration with multi-LLM offline fallback reliability.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
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
