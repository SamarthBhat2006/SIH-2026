# HACKATHON DEMO SCRIPT (2-MINUTE FAST RUN)
**Project:** Gen AI Platform for Automated Content Transformation (Problem Statement ID: 26154)  
**Organization:** National Technical Research Organisation (NTRO)  
**Presenter:** Hackathon Team

---

## ⏱️ Timeline & Action Flow (Total: 120 Seconds)

### 00:00 – 00:20 | Introduction & The Problem
> **Spoken:** "Good morning judges. Today intelligence and cybersecurity organizations like NTRO deal with thousands of raw incident briefs, threat reports, and policy updates daily. Transforming one verified source into multiple communication artefacts—like executive summaries, tactical advisories, and public releases—is slow, prone to hallucination, and lacks cryptographic auditability. Here is our solution: a Security-First, Multi-Artefact Gen AI Transformation Platform anchored by an append-only cryptographic blockchain ledger."

### 00:20 – 00:45 | Source Ingestion & Real-Time Security Screening
> **Action:** 
> 1. In the **Transform** dashboard, click **"Load Incident Demo"** (loads sample phishing & credential harvest report).
> 2. Point out the instant **Real-Time Security Scan**:
>    - Prompt Injection Check: Clean (or demonstrate injection detection warning on malicious input).
>    - Sensitive Pattern Detection: Identified internal IPs and admin email patterns.
>    - SHA-256 Source Hash instantly minted.
>
> **Spoken:** "Notice that before any AI processing occurs, our security engine screens for prompt injection vectors and sensitive credentials, treating all source content as untrusted input."

### 00:45 – 01:15 | Configuration & 1-to-5 Simultaneous Generation
> **Action:**
> 1. Set Audience = *Executive*, Tone = *Professional*, Detail = *Standard*, Objective = *Inform*.
> 2. Check all 5 outputs: *Executive Summary, Cybersecurity Advisory, LinkedIn Post, X/Twitter Thread, Presentation*.
> 3. Click **"Transform Content"**.
> 4. Watch the animated **Transformation Pipeline** step from Source $\to$ Security $\to$ Analysis $\to$ Transformation $\to$ Integrity Hash $\to$ Audit Ledger.
>
> **Spoken:** "With a single click, our grounded anti-hallucination engine generates 5 distinct artefacts tailored to different stakeholders without needing repetitive uploads."

### 01:15 – 01:40 | Reviewing Generated Artefacts & Interactive Deck
> **Action:**
> 1. Switch between tabs:
>    - **Executive Summary:** Show clear Situation, Risks, and Recommended Actions.
>    - **Cybersecurity Advisory:** Show structured severity, affected systems, and non-hallucinated IoCs.
>    - **LinkedIn & X Thread:** Show publication-ready social summaries with hashtags.
>    - **Presentation:** Click next/prev to show the interactive slide deck preview with speaker notes.
> 2. Demonstrate the **"Copy"** and **"Download All Artefacts"** buttons.

### 01:40 – 02:00 | Cryptographic Integrity & Blockchain Verification
> **Action:**
> 1. Switch to the **Blockchain Ledger** tab.
> 2. Show the newly minted Block containing the Source Hash and all 5 Output Hashes linked to previous blocks.
> 3. Click **"Validate Ledger Integrity"** $\to$ Show the green **"Ledger Verified — Zero Tampering Detected"** banner.
> 4. Quick glance at the **History** tab showing persistent SQLite audit log.
>
> **Spoken:** "Every single transformation produces immutable SHA-256 fingerprints chained in an append-only block ledger, giving NTRO complete mathematical provenance and non-repudiation. Thank you!"

---

## 🎯 Demo Preparation Checklist
- [ ] Ensure local virtualenv / dependencies are installed.
- [ ] Start app: `streamlit run app.py`.
- [ ] Confirm sample incident file loads cleanly.
- [ ] Have test malicious prompt ready for optional security injection demo.
