"""
UI Design System & Light Sketchbook Theme Styles
Inspired by Gumroad Design System (Warm Canvas Cream, Paper White Cards, Ink Black, Pink Coin & Highlight Accents).
"""

def get_custom_css() -> str:
    """Returns custom CSS implementing the Gumroad-inspired light aesthetic."""
    return """
    <style>
    /* Google Fonts: Inter with tight tracking */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        --color-canvas-cream: #f4f4f0;
        --color-paper-white: #ffffff;
        --color-ink-black: #000000;
        --color-graphite: #242423;
        --color-hairline: #d1d5dc;
        --color-coin-pink: #ff90e8;
        --color-highlight-yellow: #ffc900;
        --color-highlight-lime: #f1f333;
        --color-highlight-vermillion: #dc341e;
        --font-main: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }

    /* Global Body & Background */
    html, body, .stApp {
        background-color: var(--color-canvas-cream) !important;
        color: var(--color-ink-black) !important;
        font-family: var(--font-main) !important;
        -webkit-font-smoothing: antialiased;
    }

    [data-testid="stSidebar"] {
        background-color: #ededeb !important;
        border-right: 1px solid var(--color-hairline) !important;
    }

    [data-testid="stSidebar"] * {
        color: var(--color-ink-black) !important;
    }

    /* Headings with tight negative tracking */
    h1, h2, h3, h4, h5, h6 {
        font-family: var(--font-main) !important;
        color: var(--color-ink-black) !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
    }

    p, span, label, div {
        color: var(--color-graphite);
    }

    code, pre, .mono-text {
        font-family: var(--font-mono) !important;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }

    /* Top Header Banner */
    .gumroad-header {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 16px;
        padding: 1.75rem 2rem;
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: none !important;
    }

    .gumroad-title {
        font-size: 1.75rem;
        font-weight: 800;
        color: var(--color-ink-black);
        margin: 0;
        letter-spacing: -0.035em;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .gumroad-subtitle {
        color: var(--color-graphite);
        font-size: 0.92rem;
        margin-top: 0.35rem;
        font-weight: 400;
        letter-spacing: -0.01em;
    }

    .coin-badge {
        background-color: var(--color-coin-pink);
        color: var(--color-ink-black);
        border: 1px solid var(--color-ink-black);
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Paper White Cards */
    .paper-card {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: none !important;
    }

    .paper-card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--color-ink-black);
        margin-bottom: 0.75rem;
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Security Warning / Alert (Vermillion Highlight) */
    .alert-vermillion {
        background-color: #fff0ee;
        border: 1px solid #f8b4ab;
        border-left: 4px solid var(--color-highlight-vermillion);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }

    .alert-vermillion-title {
        color: var(--color-highlight-vermillion);
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Sensitive Data Notice (Yellow Highlight) */
    .alert-yellow {
        background-color: #fffbe6;
        border: 1px solid #ffe58f;
        border-left: 4px solid var(--color-highlight-yellow);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }

    .alert-yellow-title {
        color: #946c00;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Hash Chip */
    .hash-chip {
        background-color: var(--color-canvas-cream);
        border: 1px solid var(--color-hairline);
        color: var(--color-ink-black);
        padding: 0.35rem 0.65rem;
        border-radius: 4px;
        font-family: var(--font-mono);
        font-size: 0.8rem;
        font-weight: 500;
        word-break: break-all;
        display: inline-block;
    }

    /* Stepper / Pipeline */
    .pipeline-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 16px;
        padding: 1.1rem 1.5rem;
        margin: 1.25rem 0;
        overflow-x: auto;
    }

    .pipeline-step {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        flex: 1;
        min-width: 90px;
    }

    .pipeline-icon {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
        border: 1px solid var(--color-hairline);
        background-color: var(--color-canvas-cream);
        color: var(--color-graphite);
    }

    .step-active .pipeline-icon {
        background-color: var(--color-coin-pink);
        border-color: var(--color-ink-black);
        color: var(--color-ink-black);
    }

    .step-complete .pipeline-icon {
        background-color: var(--color-ink-black);
        border-color: var(--color-ink-black);
        color: #ffffff;
    }

    .pipeline-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--color-ink-black);
        letter-spacing: -0.01em;
    }

    .pipeline-arrow {
        color: var(--color-hairline);
        font-size: 1.1rem;
        padding: 0 0.5rem;
    }

    /* Slide Deck Card */
    .slide-card {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-top: 4px solid var(--color-ink-black);
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1rem;
        min-height: 260px;
    }

    .slide-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: var(--color-ink-black);
        letter-spacing: -0.025em;
        margin-bottom: 1rem;
    }

    .speaker-notes-box {
        background-color: var(--color-canvas-cream);
        border: 1px solid var(--color-hairline);
        border-radius: 8px;
        padding: 0.9rem 1.1rem;
        margin-top: 1.25rem;
        font-size: 0.88rem;
        color: var(--color-graphite);
    }

    /* Verification Pill */
    .verified-pill {
        background-color: var(--color-canvas-cream);
        color: var(--color-ink-black);
        border: 1px solid var(--color-ink-black);
        padding: 0.3rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Metric Box */
    .metric-box {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.5rem;
        font-weight: 800;
        color: var(--color-ink-black);
        letter-spacing: -0.03em;
    }

    .metric-title {
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--color-graphite);
        text-transform: uppercase;
        letter-spacing: 0.03em;
        margin-top: 0.25rem;
    }

    /* Buttons Styling */
    .stButton > button {
        border-radius: 4px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        letter-spacing: -0.01em !important;
        padding: 0.5rem 1.2rem !important;
        transition: all 0.15s ease !important;
    }

    .stButton > button[kind="primary"], button[data-testid="baseButton-primary"] {
        background-color: var(--color-ink-black) !important;
        color: #ffffff !important;
        border: 1px solid var(--color-ink-black) !important;
    }

    .stButton > button[kind="primary"]:hover, button[data-testid="baseButton-primary"]:hover {
        background-color: #242423 !important;
        border-color: #242423 !important;
        color: #ffffff !important;
    }

    .stButton > button[kind="secondary"], button[data-testid="baseButton-secondary"] {
        background-color: var(--color-paper-white) !important;
        color: var(--color-ink-black) !important;
        border: 1px solid var(--color-hairline) !important;
    }

    .stButton > button[kind="secondary"]:hover, button[data-testid="baseButton-secondary"]:hover {
        border-color: var(--color-ink-black) !important;
        color: var(--color-ink-black) !important;
    }

    /* Download Buttons */
    .stDownloadButton > button {
        background-color: var(--color-paper-white) !important;
        color: var(--color-ink-black) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: 4px !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
    }

    .stDownloadButton > button:hover {
        border-color: var(--color-ink-black) !important;
    }

    /* Inputs, Textareas, Selectboxes */
    .stTextArea textarea, .stTextInput input, .stSelectbox [data-baseweb="select"] {
        background-color: var(--color-paper-white) !important;
        color: var(--color-ink-black) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: 4px !important;
    }

    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--color-ink-black) !important;
        box-shadow: none !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 8px !important;
        border-bottom: 1px solid var(--color-hairline) !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: var(--color-graphite) !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        border-radius: 4px 4px 0 0 !important;
        padding: 8px 16px !important;
    }

    .stTabs [aria-selected="true"] {
        color: var(--color-ink-black) !important;
        border-bottom: 2px solid var(--color-ink-black) !important;
    }

    /* Expanders */
    .streamlit-expanderHeader {
        background-color: var(--color-paper-white) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: 8px !important;
        color: var(--color-ink-black) !important;
        font-weight: 600 !important;
    }
    </style>
    """
