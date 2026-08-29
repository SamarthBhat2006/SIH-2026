"""
UI Design System — Faithful Gumroad Style Reference Implementation
Based on: design/DESIGN (1).md

Color tokens, type scale, spacing, and component rules all sourced directly
from the spec: #f4f4f0 canvas, Inter as ABC Favorit substitute, negative tracking
at every type size, 4px radii on inputs/buttons, 16-24px on cards, zero shadows.
"""

def get_custom_css() -> str:
    """Returns CSS exactly matching the Gumroad style reference."""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,400;0,14..32,500;0,14..32,700;0,14..32,900&family=JetBrains+Mono:wght@400;600;700&display=swap');

    /* === DESIGN TOKENS === */
    :root {
        /* Colors */
        --color-canvas-cream:       #f4f4f0;
        --color-paper-white:        #ffffff;
        --color-ink-black:          #000000;
        --color-graphite:           #242423;
        --color-hairline:           #d1d5dc;
        --color-coin-pink:          #ff90e8;
        --color-highlight-yellow:   #ffc900;
        --color-highlight-lime:     #f1f333;
        --color-highlight-vermillion: #dc341e;

        /* Typography — Inter as ABC Favorit substitute */
        --font-main:   'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        --font-mono:   'JetBrains Mono', monospace;

        /* Type scale (from spec) */
        --text-caption:     14px;     /* lh 1.43, ls -0.028px */
        --text-body-sm:     16px;     /* lh 1.50, ls -0.064px */
        --text-body:        18px;     /* lh 1.56, ls -0.108px */
        --text-subheading:  24px;     /* lh 1.33, ls -0.264px */
        --text-heading-sm:  30px;     /* lh 1.38, ls -0.39px  */
        --text-heading:     36px;     /* lh 1.40, ls -0.612px */
        --text-heading-lg:  48px;     /* lh 1.25, ls -0.96px  */
        --text-display:     72px;     /* lh 1.00, ls -2.4px   */

        /* Spacing (base 4px) */
        --spacing-4: 4px;    --spacing-8: 8px;    --spacing-12: 12px;
        --spacing-16: 16px;  --spacing-24: 24px;  --spacing-32: 32px;
        --spacing-40: 40px;  --spacing-48: 48px;  --spacing-64: 64px;

        /* Border radius */
        --radius-card:  16px;
        --radius-tile:  24px;
        --radius-input: 4px;
        --radius-btn:   4px;
    }

    /* Streamlit toolbar & header styling */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        color: var(--color-ink-black) !important;
        z-index: 99 !important;
    }
    #MainMenu { display: none !important; }
    footer { display: none !important; }

    html, body, .stApp, [data-testid="stAppViewContainer"], .main {
        background-color: var(--color-canvas-cream) !important;
        color: var(--color-graphite) !important;
        font-family: var(--font-main) !important;
        font-size: var(--text-body-sm) !important;
        line-height: 1.5 !important;
        letter-spacing: -0.064px !important;
        -webkit-font-smoothing: antialiased;
        font-feature-settings: "ss04" on, "ss11" on;
    }

    .block-container {
        max-width: 1200px !important;
        padding-top: var(--spacing-8) !important;
        padding-bottom: var(--spacing-64) !important;
        padding-left: var(--spacing-32) !important;
        padding-right: var(--spacing-32) !important;
    }

    /* === SIDEBAR — collapsible with clean styling === */
    [data-testid="stSidebar"] {
        background-color: #ecece8 !important;
        border-right: 1px solid var(--color-hairline) !important;
    }

    /* Keep collapse/expand button visible and styled cleanly */
    [data-testid="stSidebarCollapseButton"],
    button[data-testid="collapsedControl"],
    [data-testid="stSidebarUserContent"] button {
        color: var(--color-ink-black) !important;
    }

    button[data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        background-color: var(--color-paper-white) !important;
        border: 1.5px solid var(--color-ink-black) !important;
        border-radius: 6px !important;
        box-shadow: 2px 2px 0 var(--color-ink-black) !important;
        margin: 8px 12px !important;
        z-index: 100 !important;
    }

    /* === TOP NAV BAR === */
    .gumroad-nav-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--color-canvas-cream);
        border-bottom: 1px solid var(--color-hairline);
        padding: var(--spacing-12) 0;
        margin-bottom: var(--spacing-24);
    }

    .gumroad-brand-group {
        display: flex;
        align-items: center;
        gap: var(--spacing-12);
    }

    /* Wordmark: tight tracking like the spec */
    .gumroad-logo {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--color-ink-black);
        letter-spacing: -0.034em;
        line-height: 1;
    }

    .gumroad-stat-pill {
        background-color: var(--color-paper-white);
        border: 1.5px solid var(--color-ink-black);
        color: var(--color-ink-black);
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: var(--text-caption);
        font-weight: 700;
        letter-spacing: -0.02em;
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }

    .gumroad-nav-links {
        display: flex;
        align-items: center;
        gap: var(--spacing-8);
    }

    .nav-pill-active {
        background-color: var(--color-ink-black) !important;
        color: var(--color-paper-white) !important;
        padding: 6px 16px !important;
        border-radius: 9999px !important;
        font-size: var(--text-body-sm) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
        border: 1.5px solid var(--color-ink-black) !important;
        cursor: pointer;
    }

    .nav-link-item {
        background-color: var(--color-paper-white) !important;
        color: var(--color-graphite) !important;
        font-size: var(--text-body-sm) !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
        padding: 6px 14px !important;
        border-radius: 9999px !important;
        border: 1px solid var(--color-hairline) !important;
        cursor: pointer;
        transition: all 0.15s ease;
    }

    .nav-link-item:hover {
        border-color: var(--color-ink-black) !important;
        color: var(--color-ink-black) !important;
    }

    /* Top navbar button container */
    div[data-testid="stHorizontalBlock"]:has(.top-nav-btn) {
        align-items: center !important;
    }

    /* === HERO SECTION === */
    .gumroad-hero-container {
        text-align: center;
        padding: var(--spacing-48) var(--spacing-24) var(--spacing-40);
        margin-bottom: var(--spacing-32);
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    /* Force Streamlit's own markdown wrapper divs to honor centering inside the hero */
    .gumroad-hero-container div[data-testid="stMarkdownContainer"],
    .gumroad-hero-container > div,
    .gumroad-hero-container p {
        text-align: center !important;
        width: 100% !important;
        max-width: none !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* Badge row — project stickers above headline */
    .hero-stickers-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: var(--spacing-8);
        margin-bottom: var(--spacing-24);
    }

    .project-sticker {
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: var(--text-caption);
        font-weight: 700;
        letter-spacing: -0.02em;
        border: 1.5px solid var(--color-ink-black);
        box-shadow: 2px 2px 0 var(--color-ink-black);
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }

    .sticker-pink   { background-color: var(--color-coin-pink);          color: var(--color-ink-black); transform: rotate(-1.5deg); }
    .sticker-yellow { background-color: var(--color-highlight-yellow);    color: var(--color-ink-black); transform: rotate(1.2deg);  }
    .sticker-white  { background-color: var(--color-paper-white);         color: var(--color-ink-black); transform: rotate(-0.8deg); }
    .sticker-lime   { background-color: var(--color-highlight-lime);      color: var(--color-ink-black); transform: rotate(1.5deg);  }

    /* Display headline — 72px from spec, tight tracking */
    .gumroad-hero-h1 {
        font-size: var(--text-display) !important;
        font-weight: 700 !important;
        color: var(--color-ink-black) !important;
        letter-spacing: -2.4px !important;
        line-height: 1.0 !important;
        margin: 0 auto var(--spacing-16) !important;
        max-width: 820px;
    }

    /* Hero subtitle — 18px body */
    .gumroad-hero-sub {
        font-size: var(--text-body) !important;
        color: var(--color-graphite) !important;
        letter-spacing: -0.108px;
        line-height: 1.56;
        width: 100% !important;
        max-width: 580px;
        margin: 0 auto var(--spacing-24) auto;
        text-align: center !important;
        display: block !important;
    }

    /* Artefact pill tags below subtitle */
    .artefact-pills-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: var(--spacing-8);
    }

    .artefact-pill {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        color: var(--color-graphite);
        padding: 5px 12px;
        border-radius: var(--radius-input);
        font-size: var(--text-caption);
        font-weight: 500;
        letter-spacing: -0.01em;
    }

    /* === FLAT WHITE CARDS === */
    .gumroad-box {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: var(--radius-card);
        padding: var(--spacing-24) var(--spacing-32);
        margin-bottom: var(--spacing-24);
    }

    .gumroad-box-title {
        font-size: var(--text-subheading);
        font-weight: 700;
        color: var(--color-ink-black) !important;
        letter-spacing: -0.264px;
        line-height: 1.33;
        margin-bottom: var(--spacing-16);
        display: flex;
        align-items: center;
        gap: var(--spacing-8);
    }

    /* === BUTTONS === */
    /* Filled Black — Primary */
    .stButton > button[kind="primary"],
    button[data-testid="baseButton-primary"] {
        background-color: var(--color-ink-black) !important;
        color: var(--color-paper-white) !important;
        border: none !important;
        border-radius: var(--radius-btn) !important;
        padding: 12px 24px !important;
        font-size: var(--text-body-sm) !important;
        font-weight: 500 !important;
        letter-spacing: -0.02em !important;
        cursor: pointer !important;
        box-shadow: none !important;
        transition: opacity 0.15s ease !important;
    }
    .stButton > button[kind="primary"]:hover,
    button[data-testid="baseButton-primary"]:hover {
        opacity: 0.88 !important;
    }

    /* Ghost Outline — Secondary */
    .stButton > button {
        background-color: transparent !important;
        color: var(--color-ink-black) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: var(--radius-btn) !important;
        padding: 12px 24px !important;
        font-size: var(--text-body-sm) !important;
        font-weight: 500 !important;
        letter-spacing: -0.02em !important;
        cursor: pointer !important;
        box-shadow: none !important;
        transition: border-color 0.15s ease !important;
    }
    .stButton > button:hover {
        border-color: var(--color-ink-black) !important;
    }

    /* === PIPELINE STEPPER === */
    .gumroad-stepper-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-radius: var(--radius-card);
        padding: var(--spacing-16) var(--spacing-32);
        margin-bottom: var(--spacing-32);
    }

    .step-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        flex: 1;
    }

    .step-bubble {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: var(--text-caption);
        font-weight: 700;
        margin-bottom: var(--spacing-4);
        border: 1.5px solid var(--color-hairline);
        background-color: var(--color-canvas-cream);
        color: var(--color-graphite);
        letter-spacing: -0.01em;
    }

    .step-item.active .step-bubble {
        background-color: var(--color-coin-pink);
        border-color: var(--color-ink-black);
        color: var(--color-ink-black);
        box-shadow: 2px 2px 0 var(--color-ink-black);
    }

    .step-item.done .step-bubble {
        background-color: var(--color-ink-black);
        border-color: var(--color-ink-black);
        color: var(--color-paper-white);
    }

    .step-text {
        font-size: 11px;
        font-weight: 700;
        color: var(--color-graphite) !important;
        letter-spacing: -0.01em;
        white-space: nowrap;
    }

    .step-arrow {
        color: var(--color-hairline);
        font-size: 1.1rem;
        padding: 0 var(--spacing-4);
        flex-shrink: 0;
    }

    /* === INPUTS === */
    .stTextArea textarea,
    .stTextInput input {
        background-color: var(--color-paper-white) !important;
        color: var(--color-graphite) !important;
        border: 1px solid var(--color-hairline) !important;
        border-radius: var(--radius-input) !important;
        padding: 12px 16px !important;
        font-size: var(--text-body-sm) !important;
        font-family: var(--font-main) !important;
        letter-spacing: -0.064px !important;
    }
    .stTextArea textarea:focus,
    .stTextInput input:focus {
        border-color: var(--color-ink-black) !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* === ALERT BOXES === */
    .alert-vermillion-box {
        background-color: #fff0ee;
        border: 1px solid #f8b4ab;
        border-left: 4px solid var(--color-highlight-vermillion);
        border-radius: var(--radius-input);
        padding: var(--spacing-16);
        margin-bottom: var(--spacing-16);
    }

    .alert-yellow-box {
        background-color: #fffbe6;
        border: 1px solid #ffe58f;
        border-left: 4px solid var(--color-highlight-yellow);
        border-radius: var(--radius-input);
        padding: var(--spacing-16);
        margin-bottom: var(--spacing-16);
    }

    /* === HASH BADGES === */
    .gumroad-hash {
        background-color: var(--color-canvas-cream);
        border: 1px solid var(--color-hairline);
        color: var(--color-graphite) !important;
        padding: 3px 8px;
        border-radius: var(--radius-input);
        font-family: var(--font-mono);
        font-size: 12px;
        font-weight: 600;
        word-break: break-all;
        display: inline-block;
    }

    /* === TABS === */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: var(--spacing-4) !important;
        border-bottom: 1px solid var(--color-hairline) !important;
        padding-bottom: 0 !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: var(--color-graphite) !important;
        font-weight: 500 !important;
        font-size: var(--text-body-sm) !important;
        letter-spacing: -0.02em !important;
        border-radius: var(--radius-input) var(--radius-input) 0 0 !important;
        padding: var(--spacing-8) var(--spacing-16) !important;
    }

    .stTabs [aria-selected="true"] {
        color: var(--color-ink-black) !important;
        border-bottom: 2px solid var(--color-ink-black) !important;
        font-weight: 700 !important;
    }

    /* === SLIDE DECK === */
    .slide-deck-box {
        background-color: var(--color-paper-white);
        border: 1px solid var(--color-hairline);
        border-top: 3px solid var(--color-ink-black);
        border-radius: var(--radius-card);
        padding: var(--spacing-24) var(--spacing-32);
        margin-bottom: var(--spacing-16);
    }

    .slide-deck-title {
        font-size: var(--text-heading-sm);
        font-weight: 700;
        color: var(--color-ink-black) !important;
        letter-spacing: -0.39px;
        line-height: 1.38;
        margin-bottom: var(--spacing-16);
    }

    .slide-deck-notes {
        background-color: var(--color-canvas-cream);
        border: 1px solid var(--color-hairline);
        border-radius: var(--radius-input);
        padding: var(--spacing-12) var(--spacing-16);
        margin-top: var(--spacing-24);
        font-size: var(--text-caption);
        color: var(--color-graphite) !important;
        line-height: 1.5;
    }
    </style>
    """
