# ⚡ IntelliFlow — NTRO AI Content Transformation Platform

> **Smart India Hackathon 2026 | Problem Statement #26154**
> Organisation: National Technical Research Organisation (NTRO) | Domain: Cyber & Blockchain

---

## 📌 About the Project

**IntelliFlow** is an AI-powered content transformation platform built for NTRO. It automates the conversion of raw intelligence documents — incident reports, threat advisories, and classified briefings — into multiple structured output artefacts tailored to different audiences and channels.

Instead of manually rewriting the same security intelligence for executives, technical teams, and social media, `IntelliFlow` does it all in one click — powered by LLMs and secured with a blockchain-backed audit trail.

---

## 🎯 What It Does

Upload any intelligence document (PDF, DOCX, or plain text) and instantly generate any combination of the following artefacts:

| Output Artefact | Description |
|---|---|
| 📋 **Executive Summary** | High-level briefing for senior leadership |
| 🚨 **Cybersecurity Advisory** | Technical threat notice with IoCs and mitigations |
| 💼 **LinkedIn Post** | Professional public awareness post |
| 🧵 **X (Twitter) Thread** | Multi-tweet thread for rapid dissemination |
| 📊 **Interactive Presentation Deck** | Slide-by-slide briefing outline with presenter notes |
| 📈 **PowerPoint Presentation (.pptx)** | Downloadable Microsoft PowerPoint deck generated automatically |

Each transformation is customizable by **target audience**, **tone**, and **communication objective**.

---

## 🛡️ Security Features

- **Prompt Injection Detection** — Scans input for adversarial jailbreak patterns and system role override attempts before sending to any LLM
- **Sensitive Data Masking** — Detects and flags PII, IP addresses, API keys, emails, and credentials in source documents
- **SHA-256 Content Hashing** — Cryptographic fingerprinting of every source document to ensure integrity
- **Blockchain Audit Ledger** — Every transformation is recorded as an immutable block in a local blockchain, providing tamper-evident provenance

---

## 🤖 AI Engine

Supports multiple LLM backends with graceful fallback:

1. **Google Gemini 2.5 Flash** (Primary) — via `google-genai` SDK
2. **OpenAI GPT-4o Mini** (Secondary fallback)
3. **Offline Simulation Engine** (Final fallback) — A deterministic, grounded generation engine that works without any API key, using content analysis to extract real facts from the source document

The provider is selected via `AI_PROVIDER` in your `.env` file (`auto` | `gemini` | `openai` | `offline_simulation`).

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) |
| **AI — Primary** | Google Gemini 2.5 Flash (`google-genai`) |
| **AI — Secondary** | OpenAI GPT-4o Mini (`openai`) |
| **Presentation Export** | `python-pptx` (PowerPoint PPTX generator) |
| **Document Parsing** | `pypdf` (PDF), `python-docx` (DOCX), `trafilatura` |
| **Blockchain Ledger** | Custom SHA-256 blockchain (`modules/blockchain.py`) |
| **Database** | SQLite via `modules/history.py` |
| **Security Scanning** | Custom regex engine (`modules/security.py`) |
| **Configuration** | `python-dotenv` |
| **Testing** | `pytest` |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure

```
SIH-2026/
├── app.py                      # Main Streamlit entrypoint
├── config/
│   └── settings.py             # Environment & app configuration
├── modules/
│   ├── ai_engine.py            # Unified LLM abstraction (Gemini / OpenAI / Offline)
│   ├── blockchain.py           # Immutable audit ledger
│   ├── content_analyzer.py     # Fact extraction from source documents
│   ├── document_processor.py   # PDF, DOCX, and text file parsing
│   ├── hashing.py              # SHA-256 document fingerprinting
│   ├── history.py              # SQLite transformation history DB
│   ├── ppt_generator.py        # Automated PowerPoint (.pptx) deck generation
│   ├── prompts.py              # LLM prompt templates
│   └── security.py             # Prompt injection & sensitive data detection
├── ui/
│   ├── dashboard.py            # Main transformation dashboard
│   ├── history_view.py         # Transformation history browser
│   ├── ledger_view.py          # Blockchain ledger explorer
│   ├── about_view.py           # About page
│   ├── components.py           # Shared UI components
│   └── styles.py               # Custom CSS (Gumroad Design System)
├── data/
│   ├── transformations.db      # SQLite history database
│   └── blockchain_ledger.json  # Persistent blockchain ledger
├── tests/                      # pytest test suite
├── sample_data/                # Sample documents for demo
├── requirements.txt
└── .env.example                # Environment variable template
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/SamarthBhat2006/SIH-2026.git
cd SIH-2026
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
cp .env.example .env
# Edit .env and add your API keys (optional — works offline without them)
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 🔑 Environment Variables

| Variable | Description | Default |
|---|---|---|
| `GEMINI_API_KEY` | Google Gemini API key | *(optional)* |
| `OPENAI_API_KEY` | OpenAI API key | *(optional)* |
| `AI_PROVIDER` | Provider selection (`auto`, `gemini`, `openai`, `offline_simulation`) | `auto` |
| `STRICT_INJECTION_BLOCKING` | Block inputs with injection risk | `false` |
| `ENABLE_SENSITIVE_DATA_MASKING` | Redact sensitive findings | `false` |
| `APP_PORT` | Streamlit port | `8501` |
| `DB_PATH` | SQLite database path | `data/transformations.db` |
| `LEDGER_PATH` | Blockchain ledger path | `data/blockchain_ledger.json` |

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 👥 Team

Built for **Smart India Hackathon 2026** — Problem Statement ID `26154`.

---

*National Technical Research Organisation (NTRO) © 2026*