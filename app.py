"""
NTRO Gen AI Platform for Automated Content Transformation
Main Streamlit Application Entrypoint
Problem Statement ID: 26154 | Organization: NTRO
Faithfully styled with the Gumroad Design System.
"""

import streamlit as st
from config.settings import DB_PATH, LEDGER_PATH
from modules.blockchain import BlockchainLedger
from modules.history import TransformationHistoryDB
from ui.styles import get_custom_css
from ui.components import render_top_navbar
from ui.dashboard import render_dashboard
from ui.history_view import render_history_view
from ui.ledger_view import render_ledger_view
from ui.about_view import render_about_view

# Configure Streamlit Page
st.set_page_config(
    page_title="transform — NTRO AI Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Gumroad Styles
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

# Sidebar Navigation (Minimalist Gumroad Style)
st.sidebar.markdown("""
<div style="padding: 0.5rem 0 1.25rem 0;">
    <div style="font-size: 1.4rem; font-weight: 900; color: #000000; letter-spacing: -0.04em;">
        transform
    </div>
    <div style="font-size: 0.8rem; color: #575756; margin-top: 2px;">
        NTRO PS #26154 • Cyber & Blockchain
    </div>
</div>
""", unsafe_allow_html=True)

nav_choice = st.sidebar.radio(
    "Navigation:",
    [
        "Dashboard",
        "History",
        "Ledger",
        "About"
    ]
)

st.sidebar.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1.25rem 0;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='font-weight: 800; font-size: 0.85rem; color: #000000; margin-bottom: 0.5rem;'>System Status</div>", unsafe_allow_html=True)

summary = ledger.get_chain_summary()
status_badge = "🟢 Valid" if summary["is_valid"] else "🔴 Tampered"
st.sidebar.markdown(f"**Ledger:** {status_badge}")
st.sidebar.markdown(f"**Total Blocks:** `{summary['total_blocks']}`")
st.sidebar.markdown(f"**Audit Records:** `{history_db.get_total_count()}`")

st.sidebar.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1.5rem 0;'>", unsafe_allow_html=True)
st.sidebar.caption("National Technical Research Organisation © 2026")

# Render Top Nav Bar on Main Page
render_top_navbar(current_view=nav_choice)

# Route to Selected View
if nav_choice == "Dashboard":
    render_dashboard(ledger, history_db)
elif nav_choice == "History":
    render_history_view(history_db)
elif nav_choice == "Ledger":
    render_ledger_view(ledger)
elif nav_choice == "About":
    render_about_view()
