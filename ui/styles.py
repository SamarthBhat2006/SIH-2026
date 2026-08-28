"""
UI Design System & Light Sketchbook Theme Styles
Faithfully implements the Gumroad design philosophy (Warm Canvas Cream #f4f4f0, Paper White Cards #ffffff, Ink Black #000000, Coin Pink #ff90e8, Graphite #242423, Hairline #d1d5dc).
"""

def get_custom_css() -> str:
    """Returns ultra-specific CSS overriding all Streamlit elements with the Gumroad sketchbook style."""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    /* 1. Global Reset & Theme Override */
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

    /* Force all app containers to warm cream */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stToolbar"], .main {
        background-color: var(--color-canvas-cream) !important;
        color: var(--color-ink-black) !important;
        font-family: var(--font-main) !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ededeb !important;
        border-right: 1px solid var(--color-hairline) !important;
    }
    [data-testid="stSidebar"] * {
        color: var(--color-ink-black) !important;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: var(--font-main) !important;
        color: var(--color-ink-black) !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
        line-height: 1.2 !important;
    }

    p, span, label, li, td, th {
        color: var(--color-graphite) !important;
        font-family: var(--font-main) !important;
    }

    code, pre {
        font-family: var(--font-mono) !important;
    }

    /* Max Width & Padding */
    .block-container {
        max-width: 1200px !important;
        padding-top: 1.5rem !important;
        padding-bottom: 4rem !important;
    }

    /* Header Banner Component */
    .gumroad-hero {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 24px;
        padding: 2.25rem 2.5rem;
        margin-bottom: 1.75rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        overflow: hidden;
    }

    .gumroad-hero::after {
        content: "G";
        position: absolute;
        right: -15px;
        bottom: -25px;
        font-size: 140px;
        font-weight: 900;
        color: rgba(255, 144, 232, 0.18);
        pointer-events: none;
        user-select: none;
        line-height: 1;
    }

    .gumroad-hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: var(--color-ink-black);
        letter-spacing: -0.04em;
        margin: 0 0 0.4rem 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .gumroad-hero-subtitle {
        font-size: 0.98rem;
        color: var(--color-graphite);
        font-weight: 400;
        max-width: 680px;
        line-height: 1.5;
        margin: 0;
    }

    .coin-sticker {
        background-color: var(--color-coin-pink);
        color: var(--color-ink-black);
        border: 1.5px solid var(--color-ink-black);
        padding: 0.45rem 1rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transform: rotate(-2deg);
        box-shadow: 2px 2px 0px var(--color-ink-black);
    }

    /* Feature & Section Cards */
    .gumroad-card {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
    }

    .gumroad-card-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--color-ink-black);
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Pipeline / Stepper */
    .gumroad-stepper {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .stepper-node {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        flex: 1;
    }

    .stepper-circle {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        border: 1.5px solid var(--color-hairline);
        background-color: var(--color-canvas-cream);
        color: var(--color-graphite);
    }

    .node-complete .stepper-circle {
        background-color: var(--color-ink-black);
        border-color: var(--color-ink-black);
        color: #ffffff;
    }

    .node-active .stepper-circle {
        background-color: var(--color-coin-pink);
        border-color: var(--color-ink-black);
        color: var(--color-ink-black);
        box-shadow: 2px 2px 0px var(--color-ink-black);
    }

    .stepper-title {
        font-size: 0.78rem;
        font-weight: 600;
        color: var(--color-ink-black);
        letter-spacing: -0.01em;
    }

    .stepper-divider {
        color: var(--color-hairline);
        font-size: 1.2rem;
        padding: 0 0.5rem;
    }

    /* Security Notice (Vermillion & Yellow) */
    .banner-injection {
        background-color: #fff0ee;
        border: 1px solid #f8b4ab;
        border-left: 5px solid var(--color-highlight-vermillion);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
    }

    .banner-injection-title {
        color: var(--color-highlight-vermillion);
        font-weight: 800;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }

    .banner-sensitive {
        background-color: #fffbe6;
        border: 1px solid #ffe58f;
        border-left: 5px solid var(--color-highlight-yellow);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
    }

    .banner-sensitive-title {
        color: #946c00;
        font-weight: 800;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }

    /* Hash Pill */
    .gumroad-hash-badge {
        background-color: var(--color-canvas-cream);
        border: 1px solid var(--color-hairline);
        color: var(--color-ink-black) !important;
        padding: 0.35rem 0.7rem;
        border-radius: 4px;
        font-family: var(--font-mono);
        font-size: 0.8rem;
        font-weight: 600;
        word-break: break-all;
        display: inline-block;
    }

    /* Buttons Overrides */
    .stButton > button {
        border-radius: 4px !important;
        font-family: var(--font-main) !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        padding: 0.55rem 1.25rem !important;
        transition: all 0.15s ease !important;
        border: 1px solid var(--color-hairline) !important;
        background-color: var(--color-paper-white) !important;
        color: var(--color-ink-black) !important;
    }

    .stButton > button:hover {
        border-color: var(--color-ink-black) !important;
        color: var(--color-ink-black) !important;
    }

    .stButton > button[kind="primary"], button[data-testid="baseButton-primary"] {
        background-color: var(--color-ink-black) !important;
        color: #ffffff !important;
        border: 1px solid var(--color-ink-black) !important;
        box-shadow: 2px 2px 0px rgba(0, 0, 0, 0.2) !important;
    }

    .stButton > button[kind="primary"]:hover, button[data-testid="baseButton-primary"]:hover {
        background-color: #242423 !important;
        color: #ffffff !important;
    }

    /* Input & Textarea Elements */
    .stTextArea textarea, .stTextInput input {
        background-color: var(--color-paper-white) !important;
        color: var(--color-ink-black) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: 4px !important;
        font-family: var(--font-main) !important;
        font-size: 0.92rem !important;
    }

    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--color-ink-black) !important;
        box-shadow: none !important;
    }

    /* Selectboxes */
    div[data-baseweb="select"] {
        background-color: var(--color-paper-white) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: 4px !important;
    }
    div[data-baseweb="select"] * {
        color: var(--color-ink-black) !important;
    }

    /* Tabs Override */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 8px !important;
        border-bottom: 2px solid var(--color-hairline) !important;
        padding-bottom: 0px !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: var(--color-graphite) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        border-radius: 4px 4px 0 0 !important;
        padding: 10px 18px !important;
    }

    .stTabs [aria-selected="true"] {
        color: var(--color-ink-black) !important;
        border-bottom: 2px solid var(--color-ink-black) !important;
        font-weight: 800 !important;
    }

    /* Metric Cards */
    .stat-tile {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: 12px;
        padding: 1.1rem;
        text-align: center;
    }

    .stat-number {
        font-size: 1.6rem;
        font-weight: 900;
        color: var(--color-ink-black);
        letter-spacing: -0.04em;
    }

    .stat-label {
        font-size: 0.78rem;
        font-weight: 600;
        color: var(--color-graphite);
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 0.2rem;
    }

    /* Slide Card */
    .slide-paper-card {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-top: 4px solid var(--color-ink-black);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.25rem;
    }

    .slide-paper-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: var(--color-ink-black);
        letter-spacing: -0.03em;
        margin-bottom: 1.1rem;
    }

    .slide-speaker-notes {
        background-color: var(--color-canvas-cream);
        border: 1px solid var(--color-hairline);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-top: 1.5rem;
        font-size: 0.9rem;
        color: var(--color-graphite);
    }
    </style>
    """
