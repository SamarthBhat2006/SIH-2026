"""
NTRO Gen AI Platform for Automated Content Transformation
Main Streamlit Application Entrypoint
Problem Statement ID: 26154 | Organization: NTRO
Styled with Gumroad-inspired clean light design system.
"""

import streamlit as st
from config.settings import DB_PATH, LEDGER_PATH
from modules.blockchain import BlockchainLedger
from modules.history import TransformationHistoryDB
from ui.styles import get_custom_css
from ui.components import render_header
from ui.dashboard import render_dashboard
from ui.history_view import render_history_view
from ui.ledger_view import render_ledger_view
from ui.about_view import render_about_view

# Configure Streamlit Page
st.set_page_config(
    page_title="NTRO Content Transformation Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Gumroad Light Design System
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize Persistent Singletons
@st.cache_resource
def get_blockchain_ledger() -> BlockchainLedger:
    return BlockchainLedger(LEDGER_PATH)

@st.cache_resource
def get_history_db() -> TransformationHistoryDB:
    return TransformationHistoryDB(DB_PATH)

ledger = get_blockchain_ledger()
history_db = get_history_db()

# Render Application Header
render_header()

# Sidebar Navigation
st.sidebar.markdown("""
<div style="padding: 0.5rem 0 1rem 0;">
    <div style="font-size: 1.15rem; font-weight: 800; color: #000000; letter-spacing: -0.02em;">
        ⚡ NTRO Platform
    </div>
    <div style="font-size: 0.8rem; color: #575756; margin-top: 2px;">
        PS #26154 • Blockchain & Cyber
    </div>
</div>
""", unsafe_allow_html=True)

nav_choice = st.sidebar.radio(
    "Navigation Menu:",
    [
        "⚡ Transform Dashboard",
        "📜 History & Audit Logs",
        "⛓️ Blockchain Ledger",
        "🏛️ Problem & Architecture"
    ]
)

st.sidebar.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1rem 0;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='font-weight: 700; font-size: 0.85rem; color: #000000; margin-bottom: 0.5rem;'>System Status</div>", unsafe_allow_html=True)

summary = ledger.get_chain_summary()
status_badge = "🟢 Valid" if summary["is_valid"] else "🔴 Tampered"
st.sidebar.markdown(f"**Ledger:** {status_badge}")
st.sidebar.markdown(f"**Total Blocks:** `{summary['total_blocks']}`")
st.sidebar.markdown(f"**Audit Records:** `{history_db.get_total_count()}`")

st.sidebar.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1.5rem 0;'>", unsafe_allow_html=True)
st.sidebar.caption("National Technical Research Organisation (NTRO)")

# Route to Selected View
if nav_choice == "⚡ Transform Dashboard":
    render_dashboard(ledger, history_db)
elif nav_choice == "📜 History & Audit Logs":
    render_history_view(history_db)
elif nav_choice == "⛓️ Blockchain Ledger":
    render_ledger_view(ledger)
elif nav_choice == "🏛️ Problem & Architecture":
    render_about_view()
