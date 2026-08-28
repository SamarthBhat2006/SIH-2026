"""
UI Design System & Authentic Gumroad Aesthetic Styles
Customized for NTRO Content Transformation Platform:
- Top full-width navigation bar with wordmark, badge, nav links with black active pill, and CTA button.
- Warm cream #f4f4f0 canvas background with floating project badges (AI Engine, SHA-256, Blockchain, Grounded).
- Hero headline '1 Source to 5 Artefacts' with perfectly balanced typography and zero overlapping.
- Flat paper-white #ffffff cards with 16-24px radii and crisp hairline borders (zero shadows/glows).
- Solid black #000000 filled buttons (4px radius) and ghost outline buttons.
"""

def get_custom_css() -> str:
    """Returns refined CSS matching the authentic Gumroad aesthetic tailored to NTRO."""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    :root {
        --canvas-cream: #f4f4f0;
        --paper-white: #ffffff;
        --ink-black: #000000;
        --graphite: #242423;
        --hairline: #d1d5dc;
        --coin-pink: #ff90e8;
        --highlight-yellow: #ffc900;
        --highlight-lime: #f1f333;
        --highlight-vermillion: #dc341e;
        --font-main: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }

    /* Hide default Streamlit header bar & footer */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    footer {
        display: none !important;
    }

    /* Base Body and Containers */
    html, body, .stApp, [data-testid="stAppViewContainer"], .main {
        background-color: var(--canvas-cream) !important;
        color: var(--ink-black) !important;
        font-family: var(--font-main) !important;
        -webkit-font-smoothing: antialiased;
    }

    .block-container {
        max-width: 1260px !important;
        padding-top: 0.5rem !important;
        padding-bottom: 4rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ecece8 !important;
        border-right: 1px solid var(--hairline) !important;
    }

    /* Gumroad Top Navigation Bar */
    .gumroad-nav-wrapper {
        background-color: var(--canvas-cream);
        border-bottom: 1px solid var(--hairline);
        padding: 0.9rem 0;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .gumroad-brand-group {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .gumroad-logo {
        font-size: 1.75rem;
        font-weight: 900;
        color: var(--ink-black);
        letter-spacing: -0.045em;
        text-decoration: none;
    }

    .gumroad-stat-pill {
        background-color: var(--paper-white);
        border: 1.5px solid var(--ink-black);
        color: var(--ink-black);
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        letter-spacing: -0.01em;
    }

    .gumroad-nav-links {
        display: flex;
        align-items: center;
        gap: 18px;
    }

    .nav-pill-active {
        background-color: var(--ink-black);
        color: #ffffff !important;
        padding: 7px 16px;
        border-radius: 9999px;
        font-size: 0.9rem;
        font-weight: 700;
        text-decoration: none;
    }

    .nav-link-item {
        color: var(--graphite);
        font-size: 0.9rem;
        font-weight: 500;
        text-decoration: none;
        padding: 6px 10px;
    }

    /* Refined Hero Section */
    .gumroad-hero-container {
        text-align: center;
        padding: 2.75rem 1.5rem 2.25rem 1.5rem;
        margin-bottom: 2rem;
        background-color: var(--canvas-cream);
        position: relative;
    }

    /* Floating Project Sticker Badges */
    .hero-stickers-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 1.5rem;
    }

    .project-sticker {
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        border: 1.5px solid var(--ink-black);
        box-shadow: 2px 2px 0px var(--ink-black);
        letter-spacing: -0.01em;
    }

    .sticker-pink {
        background-color: var(--coin-pink);
        color: var(--ink-black);
        transform: rotate(-2deg);
    }

    .sticker-yellow {
        background-color: var(--highlight-yellow);
        color: var(--ink-black);
        transform: rotate(2deg);
    }

    .sticker-white {
        background-color: var(--paper-white);
        color: var(--ink-black);
        transform: rotate(-1deg);
    }

    .sticker-lime {
        background-color: var(--highlight-lime);
        color: var(--ink-black);
        transform: rotate(1.5deg);
    }

    .gumroad-hero-h1 {
        font-size: 3.8rem;
        font-weight: 900;
        color: var(--ink-black) !important;
        letter-spacing: -0.045em !important;
        line-height: 1.1 !important;
        margin: 0 auto 1rem auto !important;
        max-width: 800px;
    }

    .gumroad-hero-sub {
        font-size: 1.15rem;
        color: var(--graphite) !important;
        max-width: 650px;
        line-height: 1.6;
        margin: 0 auto 1.5rem auto;
    }

    /* Artefact Tags Pill Row */
    .artefact-pills-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 1rem;
    }

    .artefact-pill {
        background-color: var(--paper-white);
        border: 1px solid var(--hairline);
        color: var(--graphite);
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* Flat White Cards */
    .gumroad-box {
        background-color: var(--paper-white);
        border: 1px solid var(--hairline);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: none !important;
    }

    .gumroad-box-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: var(--ink-black) !important;
        letter-spacing: -0.03em;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 4px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.65rem 1.4rem !important;
        transition: all 0.15s ease !important;
        border: 1px solid var(--hairline) !important;
        background-color: var(--paper-white) !important;
        color: var(--ink-black) !important;
    }

    .stButton > button[kind="primary"], button[data-testid="baseButton-primary"] {
        background-color: var(--ink-black) !important;
        color: #ffffff !important;
        border: 1.5px solid var(--ink-black) !important;
        box-shadow: 2px 2px 0px rgba(0,0,0,0.15) !important;
    }

    .stButton > button[kind="primary"]:hover, button[data-testid="baseButton-primary"]:hover {
        background-color: #242423 !important;
        color: #ffffff !important;
    }

    .stButton > button:hover {
        border-color: var(--ink-black) !important;
        color: var(--ink-black) !important;
    }

    /* Stepper */
    .gumroad-stepper-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--paper-white);
        border: 1px solid var(--hairline);
        border-radius: 16px;
        padding: 1.1rem 1.75rem;
        margin-bottom: 2rem;
    }

    .step-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        flex: 1;
    }

    .step-bubble {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        font-weight: 800;
        margin-bottom: 0.35rem;
        border: 1.5px solid var(--hairline);
        background-color: var(--canvas-cream);
        color: var(--graphite);
    }

    .step-item.active .step-bubble {
        background-color: var(--coin-pink);
        border-color: var(--ink-black);
        color: var(--ink-black);
        box-shadow: 2px 2px 0px var(--ink-black);
    }

    .step-item.done .step-bubble {
        background-color: var(--ink-black);
        border-color: var(--ink-black);
        color: #ffffff;
    }

    .step-text {
        font-size: 0.78rem;
        font-weight: 700;
        color: var(--ink-black) !important;
        letter-spacing: -0.01em;
    }

    .step-arrow {
        color: var(--hairline);
        font-size: 1.2rem;
        padding: 0 0.5rem;
    }

    /* Inputs & Selects */
    .stTextArea textarea, .stTextInput input {
        background-color: var(--paper-white) !important;
        color: var(--ink-black) !important;
        border: 1px solid var(--hairline) !important;
        border-radius: 4px !important;
        font-size: 0.95rem !important;
    }

    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--ink-black) !important;
        box-shadow: none !important;
    }

    /* Alert Boxes */
    .alert-vermillion-box {
        background-color: #fff0ee;
        border: 1px solid #f8b4ab;
        border-left: 5px solid var(--highlight-vermillion);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }

    .alert-yellow-box {
        background-color: #fffbe6;
        border: 1px solid #ffe58f;
        border-left: 5px solid var(--highlight-yellow);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }

    /* Hash Badges */
    .gumroad-hash {
        background-color: var(--canvas-cream);
        border: 1px solid var(--hairline);
        color: var(--ink-black) !important;
        padding: 0.35rem 0.65rem;
        border-radius: 4px;
        font-family: var(--font-mono);
        font-size: 0.8rem;
        font-weight: 600;
        word-break: break-all;
        display: inline-block;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 12px !important;
        border-bottom: 2px solid var(--hairline) !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: var(--graphite) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        border-radius: 4px 4px 0 0 !important;
        padding: 10px 18px !important;
    }

    .stTabs [aria-selected="true"] {
        color: var(--ink-black) !important;
        border-bottom: 2.5px solid var(--ink-black) !important;
        font-weight: 800 !important;
    }

    /* Slide Deck Card */
    .slide-deck-box {
        background-color: var(--paper-white);
        border: 1px solid var(--hairline);
        border-top: 4px solid var(--ink-black);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.25rem;
    }

    .slide-deck-title {
        font-size: 1.45rem;
        font-weight: 800;
        color: var(--ink-black) !important;
        letter-spacing: -0.03em;
        margin-bottom: 1rem;
    }

    .slide-deck-notes {
        background-color: var(--canvas-cream);
        border: 1px solid var(--hairline);
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-top: 1.5rem;
        font-size: 0.9rem;
        color: var(--graphite) !important;
    }
    </style>
    """
