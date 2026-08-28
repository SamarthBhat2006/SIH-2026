"""
UI Design System & Cybersecurity Dark Theme Styles
Enterprise-grade styling for NTRO Gen AI Content Transformation Platform.
"""

def get_custom_css() -> str:
    """Returns custom CSS for the dark cybersecurity interface."""
    return """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');

    /* Global Base */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    code, pre, .mono-text {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 95% !important;
    }

    /* Header Banner */
    .ntro-header-container {
        background: linear-gradient(135deg, rgba(10, 25, 47, 0.95) 0%, rgba(13, 17, 23, 0.98) 100%);
        border: 1px solid rgba(0, 229, 255, 0.25);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(0, 229, 255, 0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .ntro-title {
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00e5ff, #00e676);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .ntro-subtitle {
        color: #8b949e;
        font-size: 0.88rem;
        margin-top: 0.3rem;
        font-weight: 400;
    }

    .ntro-badge {
        background: rgba(0, 229, 255, 0.1);
        color: #00e5ff;
        border: 1px solid rgba(0, 229, 255, 0.3);
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Cards */
    .cyber-card {
        background: rgba(13, 17, 23, 0.8);
        border: 1px solid rgba(48, 54, 61, 0.8);
        border-radius: 10px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(8px);
    }

    .cyber-card:hover {
        border-color: rgba(0, 229, 255, 0.3);
    }

    .cyber-card-title {
        font-size: 1rem;
        font-weight: 700;
        color: #e6edf3;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Security Warning Card */
    .sec-warning-card {
        background: linear-gradient(135deg, rgba(255, 23, 68, 0.12) 0%, rgba(20, 10, 15, 0.8) 100%);
        border: 1px solid rgba(255, 23, 68, 0.4);
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }

    .sec-warning-title {
        color: #ff5252;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Sensitive Data Notice Card */
    .sec-notice-card {
        background: linear-gradient(135deg, rgba(255, 171, 0, 0.12) 0%, rgba(20, 18, 10, 0.8) 100%);
        border: 1px solid rgba(255, 171, 0, 0.4);
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
    }

    .sec-notice-title {
        color: #ffd740;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Hash Chip */
    .hash-chip {
        background: #0d1117;
        border: 1px solid #30363d;
        color: #58a6ff;
        padding: 0.3rem 0.6rem;
        border-radius: 6px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        word-break: break-all;
        display: inline-block;
    }

    /* Stepper / Pipeline */
    .pipeline-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #0d1117;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1rem;
        margin: 1.25rem 0;
        overflow-x: auto;
    }

    .pipeline-step {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        flex: 1;
        min-width: 100px;
    }

    .pipeline-icon {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
        font-weight: bold;
        margin-bottom: 0.4rem;
        border: 2px solid;
    }

    .step-active .pipeline-icon {
        background: rgba(0, 229, 255, 0.2);
        border-color: #00e5ff;
        color: #00e5ff;
        box-shadow: 0 0 12px rgba(0, 229, 255, 0.4);
    }

    .step-complete .pipeline-icon {
        background: rgba(0, 230, 118, 0.2);
        border-color: #00e676;
        color: #00e676;
    }

    .step-idle .pipeline-icon {
        background: rgba(48, 54, 61, 0.4);
        border-color: #484f58;
        color: #8b949e;
    }

    .pipeline-label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #c9d1d9;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .pipeline-arrow {
        color: #484f58;
        font-size: 1.1rem;
        padding: 0 0.5rem;
    }

    /* Slide Deck Card */
    .slide-card {
        background: #0d1117;
        border: 1px solid #30363d;
        border-left: 4px solid #00e5ff;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        min-height: 280px;
    }

    .slide-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #00e5ff;
        margin-bottom: 1rem;
    }

    .speaker-notes-box {
        background: rgba(22, 27, 34, 0.8);
        border: 1px dashed #30363d;
        border-radius: 6px;
        padding: 0.8rem;
        margin-top: 1rem;
        font-size: 0.85rem;
        color: #8b949e;
    }

    /* Verification Pill */
    .verified-pill {
        background: rgba(0, 230, 118, 0.15);
        color: #00e676;
        border: 1px solid rgba(0, 230, 118, 0.4);
        padding: 0.25rem 0.6rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }

    /* Metric Grid */
    .metric-box {
        background: rgba(22, 27, 34, 0.6);
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 0.9rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.4rem;
        font-weight: 800;
        color: #00e5ff;
    }

    .metric-title {
        font-size: 0.75rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.2rem;
    }
    </style>
    """
