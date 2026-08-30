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
    page_title="IntelliFlow — NTRO AI Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Theme State
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Inject Custom Design System Styles (Light / Dark)
st.markdown(get_custom_css(st.session_state.theme), unsafe_allow_html=True)

# Initialize Persistent Singletons
@st.cache_resource
def get_blockchain_ledger() -> BlockchainLedger:
    return BlockchainLedger(LEDGER_PATH)

@st.cache_resource
def get_history_db() -> TransformationHistoryDB:
    return TransformationHistoryDB(DB_PATH)

ledger = get_blockchain_ledger()
history_db = get_history_db()

# Initialize Navigation State
NAV_OPTIONS = ["Dashboard", "History", "Ledger", "About"]
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "Dashboard"

# Sidebar Navigation (Interactive full-width buttons)
st.sidebar.markdown("<div style='font-weight: 800; font-size: 0.95rem; color: var(--color-ink-black); margin: 0.5rem 0 0.85rem 0;'>Navigation</div>", unsafe_allow_html=True)

nav_items_sidebar = [
    ("Dashboard", "⚡ Dashboard"),
    ("History", "📜 History"),
    ("Ledger", "🔗 Blockchain Ledger"),
    ("About", "ℹ️ About Platform"),
]

for view_key, label in nav_items_sidebar:
    is_active = (st.session_state.nav_choice == view_key)
    btn_type = "primary" if is_active else "secondary"
    if st.sidebar.button(
        label,
        key=f"sidebar_btn_{view_key.lower()}",
        type=btn_type,
        use_container_width=True
    ):
        if st.session_state.nav_choice != view_key:
            st.session_state.nav_choice = view_key
            st.rerun()

st.sidebar.markdown("<hr style='border:0; border-top:1px solid var(--color-hairline); margin: 1.25rem 0;'>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='font-weight: 800; font-size: 0.85rem; color: var(--color-ink-black); margin-bottom: 0.5rem;'>System Status</div>", unsafe_allow_html=True)

summary = ledger.get_chain_summary()
status_badge = "🟢 Valid" if summary["is_valid"] else "🔴 Tampered"
st.sidebar.markdown(f"**Ledger:** {status_badge}")
st.sidebar.markdown(f"**Total Blocks:** `{summary['total_blocks']}`")
st.sidebar.markdown(f"**Audit Records:** `{history_db.get_total_count()}`")

st.sidebar.markdown("<hr style='border:0; border-top:1px solid #d1d5dc; margin: 1.5rem 0;'>", unsafe_allow_html=True)
st.sidebar.caption("National Technical Research Organisation © 2026")

# Render Top Nav Bar on Main Page
active_view = st.session_state.nav_choice
render_top_navbar(current_view=active_view)

# Route to Selected View
if active_view == "Dashboard":
    render_dashboard(ledger, history_db)
elif active_view == "History":
    render_history_view(history_db)
elif active_view == "Ledger":
    render_ledger_view(ledger)
elif active_view == "About":
    render_about_view()

