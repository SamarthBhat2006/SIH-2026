"""
Configuration and settings module for the NTRO AI Content Transformation Platform.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
SAMPLE_DATA_DIR = BASE_DIR / "sample_data"

DATA_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)
SAMPLE_DATA_DIR.mkdir(exist_ok=True)

# Database and Ledger Paths
DB_PATH = os.getenv("DB_PATH", str(DATA_DIR / "transformations.db"))
LEDGER_PATH = os.getenv("LEDGER_PATH", str(DATA_DIR / "blockchain_ledger.json"))

# API Keys and Provider
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_PROVIDER = os.getenv("AI_PROVIDER", "auto").lower()

# Security & Guardrail Thresholds
MAX_INPUT_CHARS = 50000
MAX_UPLOAD_SIZE_MB = 10

# Supported Output Types
OUTPUT_TYPES = {
    "executive_summary": "Executive Summary",
    "cybersecurity_advisory": "Cybersecurity Advisory",
    "linkedin_post": "LinkedIn Post",
    "x_thread": "X/Twitter Thread",
    "presentation": "Interactive Presentation",
    "presentation_pptx": "Presentation / PowerPoint (.pptx)",
    "infographic": "Infographic Brief",
}

# Configuration Options
AUDIENCE_OPTIONS = [
    "Executive",
    "Technical Team",
    "General Public",
    "Security / Intelligence Analyst",
    "Social Media Audience",
    "Government/Official",
]

TONE_OPTIONS = [
    "Professional",
    "Formal",
    "Simple",
    "Engaging",
    "Analytical",
    "Informative",
    "Urgent",
    "Concise",
]

DETAIL_LEVEL_OPTIONS = [
    "Brief",
    "Standard",
    "Detailed",
]

OBJECTIVE_OPTIONS = [
    "Inform",
    "Alert",
    "Analyze",
    "Engage",
    "Summarize",
    "Educate",
    "Recommend Action",
    "Persuade",
]

# Intelligent Default Profiles mapped to Target Audience
AUDIENCE_PROFILES = {
    "Executive": {
        "tone": "Professional",
        "detail": "Brief",
        "objective": "Inform",
    },
    "Technical Team": {
        "tone": "Professional",
        "detail": "Detailed",
        "objective": "Inform",
    },
    "General Public": {
        "tone": "Simple",
        "detail": "Standard",
        "objective": "Inform",
    },
    "Security / Intelligence Analyst": {
        "tone": "Formal",
        "detail": "Detailed",
        "objective": "Analyze",
    },
    "Social Media Audience": {
        "tone": "Engaging",
        "detail": "Brief",
        "objective": "Engage",
    },
    "Government/Official": {
        "tone": "Formal",
        "detail": "Detailed",
        "objective": "Inform",
    },
}

# Sensitive Data Detection Regular Expressions
SENSITIVE_PATTERNS = {
    "Email Address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b",
    "IPv4 Address": r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
    "API Key / Secret Token": r"(?i)\b(?:api[_-]?key|secret[_-]?token|auth[_-]?token|bearer\s+[a-z0-9_\-\.]{16,}|access[_-]?token)[\s:=]+['\"]?([a-zA-Z0-9_\-\.]{16,})['\"]?\b",
    "Generic Key String": r"\b(?:ghp_[a-zA-Z0-9]{36}|AIza[0-9A-Za-z-_]{35}|sk-[a-zA-Z0-9]{32,}|AKIA[0-9A-Z]{16})\b",
    "Password Assignment": r"(?i)\b(?:password|passwd|pwd)[\s:=]+['\"]?([^\s,;'\"]{6,})['\"]?\b",
    "Phone Number": r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
}

# Prompt Injection Detection Signatures
PROMPT_INJECTION_PATTERNS = [
    r"(?i)ignore\s+(?:all\s+)?(?:previous|prior|above)\s+(?:instructions|prompts|rules|commands)",
    r"(?i)disregard\s+(?:all\s+)?(?:safety|system|prior)\s+(?:rules|instructions|prompts)",
    r"(?i)reveal\s+(?:your\s+)?(?:system\s+prompt|developer\s+instructions|secret\s+key)",
    r"(?i)system\s+override",
    r"(?i)you\s+are\s+now\s+(?:in\s+)?(?:dan\s+mode|jailbroken|unfiltered|god\s+mode)",
    r"(?i)do\s+anything\s+now",
    r"(?i)bypass\s+(?:all\s+)?(?:safety|content)\s+filters",
    r"(?i)forget\s+everything\s+you\s+were\s+told",
    r"(?i)new\s+rule:\s+you\s+must",
]
