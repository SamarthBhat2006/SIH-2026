"""
NTRO Gen AI Platform for Automated Content Transformation
Main Streamlit Application Entrypoint
Problem Statement ID: 26154 | Organization: NTRO
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
    page_title="NTRO AI Content Transformation Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Cyber Dark Styles
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
<div style="text-align: center; padding: 0.5rem 0 1rem 0;">
    <div style="font-size: 2rem;">🛡️</div>
    <strong style="color: #00e5ff; font-size: 1.1rem;">NTRO PLATFORM</strong><br>
    <span style="font-size: 0.75rem; color: #8b949e;">PS #26154 • CYBER & BLOCKCHAIN</span>
</div>
""", unsafe_allow_html=True)

nav_choice = st.sidebar.radio(
    "Navigation Menu:",
    [
        "⚡ Transform Dashboard",
        "📜 History & Audit Logs",
        "⛓️ Blockchain Ledger Explorer",
        "🏛️ Problem & Architecture"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 System Status")
summary = ledger.get_chain_summary()
status_color = "🟢" if summary["is_valid"] else "🔴"
st.sidebar.markdown(f"**Ledger Status:** {status_color} {'Valid' if summary['is_valid'] else 'Tampered'}")
st.sidebar.markdown(f"**Total Blocks:** `{summary['total_blocks']}`")
st.sidebar.markdown(f"**Total Audit Records:** `{history_db.get_total_count()}`")

st.sidebar.markdown("---")
st.sidebar.caption("National Technical Research Organisation (NTRO) © 2026")

# Route to Selected View
if nav_choice == "⚡ Transform Dashboard":
    render_dashboard(ledger, history_db)
elif nav_choice == "📜 History & Audit Logs":
    render_history_view(history_db)
elif nav_choice == "⛓️ Blockchain Ledger Explorer":
    render_ledger_view(ledger)
elif nav_choice == "🏛️ Problem & Architecture":
    render_about_view()
