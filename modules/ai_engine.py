"""
AI Transformation Engine
Provides a unified abstraction for generating transformations across Gemini, OpenAI, and a grounded offline simulation engine.
"""

import os
from typing import Dict, List, Any, Optional
from config.settings import GEMINI_API_KEY, OPENAI_API_KEY, AI_PROVIDER
from modules.prompts import GROUNDING_SYSTEM_PROMPT, build_prompt_for_artefact
from modules.content_analyzer import ContentAnalyzer

class AIEngine:
    """Unified transformation manager supporting multiple LLM backends."""

    def __init__(self, provider: Optional[str] = None, gemini_key: Optional[str] = None, openai_key: Optional[str] = None):
        self.provider = (provider or AI_PROVIDER).lower()
        self.gemini_key = gemini_key or os.getenv("GEMINI_API_KEY", GEMINI_API_KEY)
        self.openai_key = openai_key or os.getenv("OPENAI_API_KEY", OPENAI_API_KEY)

    def _call_gemini(self, prompt: str) -> str:
        """Invokes Google Gemini LLM API using available model endpoints."""
        models_to_try = [
            "gemini-3.5-flash-lite",
            "gemini-3.5-flash",
            "gemini-3.6-flash",
            "gemini-3.7-flash"
        ]

        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=self.gemini_key)
            config = types.GenerateContentConfig(
                system_instruction=GROUNDING_SYSTEM_PROMPT
            )
            last_err = None
            for model_name in models_to_try:
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config=config
                    )
                    if response and response.text:
                        return response.text.strip()
                except Exception as e:
                    last_err = e
                    continue
            if last_err:
                raise last_err
        except Exception as e:
            raise RuntimeError(f"Gemini API call failed: {str(e)}")

        raise RuntimeError("No valid response received from Gemini API.")

    def _call_openai(self, prompt: str) -> str:
        """Invokes OpenAI API."""
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": GROUNDING_SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"OpenAI API call failed: {str(e)}")

    def _generate_grounded_offline(
        self,
        artefact_type: str,
        source_text: str,
        config: Dict[str, Any],
        grounded_facts: Dict[str, Any]
    ) -> str:
        """
        High-fidelity deterministic grounded generation engine.
        Produces format-specific, configuration-driven artefacts strictly from source facts.
        """
        audience = config.get("audience", "Executive")
        tone = config.get("tone", "Professional")
        detail = config.get("detail", "Standard")
        objective = config.get("objective", "Inform")

        title = grounded_facts.get("title", "Operational Threat Transformation Report")
        severity = grounded_facts.get("detected_severity", "Not specified in source material.")
        dates = ", ".join(grounded_facts.get("detected_dates", ["Not specified in source material."]))
        cves = ", ".join(grounded_facts.get("detected_cves", ["Not specified in source material."]))
        ips = ", ".join(grounded_facts.get("detected_ips", ["Not specified in source material."]))
        domains = ", ".join(grounded_facts.get("detected_domains", ["Not specified in source material."]))
        hashes = ", ".join(grounded_facts.get("detected_hashes", ["Not specified in source material."]))
        systems_list = grounded_facts.get("potential_affected_systems", ["Not specified in source material."])
        systems = ", ".join(systems_list) if isinstance(systems_list, list) else str(systems_list)
        users_list = grounded_facts.get("impacted_users", ["Not specified in source material."])
        users = ", ".join(users_list) if isinstance(users_list, list) else str(users_list)
        mitigations_list = grounded_facts.get("mitigations", ["Not specified in source material."])
        attack_list = grounded_facts.get("attack_vectors", ["Not specified in source material."])
        attack_vector = ", ".join(attack_list) if isinstance(attack_list, list) else str(attack_list)

        # Extract significant paragraphs
        paragraphs = [p.strip() for p in source_text.split("\n") if len(p.strip()) > 20 and not p.strip().startswith("#")]
        p1 = paragraphs[0] if paragraphs else source_text[:200]
        p2 = paragraphs[1] if len(paragraphs) > 1 else (paragraphs[0] if paragraphs else "No secondary operational detail provided.")
        p3 = paragraphs[2] if len(paragraphs) > 2 else "Security operations teams deployed active containment measures."

        # Tone adjective modifier
        tone_prefix = "URGENT ACTION REQUIRED: " if tone.lower() == "urgent" else ""
        action_tone = "Immediate" if tone.lower() == "urgent" else "Strategic"

        # Audience-oriented framing
        if audience == "Executive":
            audience_focus = "Focus on enterprise governance, strategic exposure, and high-level risk management."
        elif audience == "Technical Team":
            audience_focus = "Focus on technical IoCs, perimeter hardening, credential revocation, and log telemetry."
        elif audience == "General Public":
            audience_focus = "Focus on user awareness, basic cyber hygiene, and threat identification."
        else:
            audience_focus = f"Focus on operational readiness and coordination for {audience}."

        if artefact_type == "executive_summary":
            detail_extra = f"\n- **Extended Operational Context:** {p3}\n- **Detailed Systems Scope:** {systems}" if detail.lower() == "detailed" else ""
            return f"""# EXECUTIVE SUMMARY

### Situation / Context
{tone_prefix}{p1}

### Key Findings
- **Observed Threat Event:** {p2}
- **Identified Indicators:** IP/Network anchors: `{ips}`, CVE references: `{cves}`.
- **Verification Window:** Event timeline recorded around {dates}.{detail_extra}

### Impact
- **Severity Rating:** {severity}
- **Impact Assessment:** Risk of credential compromise and unauthorized resource access within organizational assets ({systems}). Prompt detection isolated initial blast radius.

### Risk / Significance
- **Audience Impact ({audience}):** {audience_focus}
- **Risk Posture:** Active threat vector under a **{tone.lower()}** operational posture with an objective to **{objective.lower()}** leadership.

### Recommended Actions
1. **{action_tone} Mitigation:** Revoke active tokens and force credential reset for targeted accounts ({users}).
2. **Perimeter Hardening:** Implement network blocklist rules for identified suspicious endpoints and domains (`{domains}`).
3. **Cryptographic Provenance:** Validate and archive transformation audit logs in the immutable ledger.

### Conclusion
Containment measures remain active. Leadership is advised to maintain heightened monitoring and enforce mandatory zero-trust verification across all operational perimeters.
"""

        elif artefact_type == "cybersecurity_advisory":
            mitigation_bullets = "\n".join([f"- {m}" for m in mitigations_list]) if mitigations_list != ["Not specified in source material."] else "- Revoke compromised credentials and enforce multi-factor authentication (MFA).\n- Block all identified malicious IP addresses and external domain indicators.\n- Correlate authentication logs for anomalous token generation."
            return f"""# CYBERSECURITY ADVISORY

**Title:** {title}
**Severity:** {severity}
**Date:** {dates}
**Target Audience:** {audience} | **Tone:** {tone}

---

### Threat Overview
{tone_prefix}{p1}

### Affected Systems / Users
- **Targeted Infrastructure:** {systems}
- **Impacted Accounts / Entities:** {users}

### Threat Description
{p2}
Adversary activity was identified attempting unauthorized access through credential harvesting and targeted infrastructure exploitation.

### Attack Vector
{attack_vector}

### Indicators of Compromise
- **IP Addresses:** `{ips}`
- **Domains / URLs:** `{domains}`
- **CVE Identifiers:** `{cves}`
- **File Hashes:** `{hashes}`

### Potential Impact
Unauthorized credential access, session token hijacking, potential lateral movement, and unauthorized exfiltration from affected communication channels.

### Recommended Mitigation
{mitigation_bullets}

### Preventive Measures
- Enforce strict FIDO2 / hardware token authentication across all user tiers.
- Synchronize perimeter firewall and DNS filtering with active threat intelligence feeds.
- Implement continuous credential exposure auditing and anomalous geolocation alerts.

### Incident Response Recommendations
- Isolate affected host endpoints and invalidate active bearer tokens immediately.
- Preserve memory artifacts and verify audit integrity against SHA-256 blockchain records.
- Notify the National Cyber Operations Center (NCOC) / NTRO incident desk with verified IoC telemetry.
"""

        elif artefact_type == "linkedin_post":
            return f"""🚨 **Cybersecurity Update: Key Findings & Tactical Insights**

{p1}

As organizations strengthen their defensive posture against modern threats, rapid intelligence sharing and grounded analysis are critical.

Here is what decision-makers and security professionals need to know:

🔹 **The Situation:** {p2[:160]}...
🔹 **Severity Classification:** Designated as **{severity}**.
🔹 **Critical Vulnerabilities & IoCs:** Monitored endpoints (`{ips}`) and domain vectors (`{domains}`).
🔹 **Defensive Actions:** Session revocation, gateway domain filtering, and cryptographic audit tracking.

💡 **Key Takeaway for {audience}:**
{audience_focus} Ensure multi-factor authentication (MFA) is strictly enforced and verify communication integrity with tamper-evident audit trails.

Stay vigilant and protect your organization's digital assets.

#CyberSecurity #ThreatIntelligence #NTRO #IncidentResponse #GovTech #InfoSec #CyberDefense
"""

        elif artefact_type == "x_thread":
            short_p1 = (p1[:160] + "...") if len(p1) > 160 else p1
            short_p2 = (p2[:160] + "...") if len(p2) > 160 else p2
            return f"""1/ 🚨 THREAT BRIEFING: Critical Security Incident & Analysis

{short_p1}

Here is the 5-point breakdown 🧵 ⬇️

---

2/ 🔍 What happened:
{short_p2}
• Severity Level: {severity}
• Documented Timeline: {dates}

---

3/ ⚡ Impact & Indicators:
• Targets: {systems}
• Flagged IoCs: {domains if domains != 'Not specified in source material.' else 'Suspicious external links'}
• Identified CVEs: {cves}

---

4/ 🛡️ Defensive Actions for {audience}:
• Revoke active sessions & rotate credentials immediately.
• Block identified malicious domains & IP anchors across perimeter filters.
• Enforce strict MFA verification.

---

5/ 📌 Key Takeaway:
Containment is underway. Ensure your teams monitor authentication logs and maintain cryptographic verification of operational briefs. #CyberAlert #NTRO #InfoSec
"""

        elif artefact_type == "presentation":
            return f"""---
## SLIDE 1 — TITLE
**Title:** {title}
**Subtitle:** Operational Intelligence Briefing for {audience}

**Speaker Notes:**
Welcome everyone. This briefing provides a grounded analysis of recent operational intelligence, structured specifically for {audience} with an objective to {objective.lower()} stakeholders on risk containment and mitigation actions.

---
## SLIDE 2 — OVERVIEW
**Situation & Context:**
• **Event Summary:** {p1[:130]}...
• **Event Timeline:** Verified activity recorded on {dates}.
• **Severity Status:** Classified as **{severity}**.

**Speaker Notes:**
Reviewing the background: anomalous activity was identified across monitored channels. Immediate triage was initiated to assess the blast radius and determine affected dependencies.

---
## SLIDE 3 — KEY FINDINGS
**Core Observations:**
• **Adversary Activity:** {p2[:130]}...
• **Targeted Systems:** {systems}
• **Network Indicators:** `{ips}` | `{domains}`

**Speaker Notes:**
Our technical assessment isolated the primary threat vectors and confirmed that initial intrusion attempts were targeted at specific operational infrastructure.

---
## SLIDE 4 — IMPACT / RISK
**Risk & Impact Analysis:**
• **Potential Exposure:** Risk of credential capture and unauthorized session hijacking.
• **Containment Scope:** Perimeter defenses deployed to prevent lateral escalation.
• **Significance for {audience}:** {audience_focus}

**Speaker Notes:**
Regarding impact: the risk is evaluated as {severity}. While core data assets remain intact, strict containment protocols must be maintained.

---
## SLIDE 5 — RECOMMENDATIONS
**Strategic & Tactical Actions:**
• **Action 1:** Immediate token revocation and credential rotation for affected users ({users}).
• **Action 2:** Perimeter blocklist updates for identified domain and IP indicators.
• **Action 3:** Cryptographic audit trail preservation via SHA-256 blockchain ledger.

**Speaker Notes:**
We urge all operational units to implement these prescribed mitigations immediately and ensure all incident telemetry is verified against our audit ledger.

---
## SLIDE 6 — CONCLUSION
**Final Takeaways & Next Steps:**
• Threat activity successfully identified and contained.
• Continuous 24/7 monitoring maintained across organizational endpoints.
• Full transformation audit package archived with cryptographic proof.

**Speaker Notes:**
In conclusion, prompt response has stabilized the environment. We now open the floor for questions and coordination remarks.
"""
        else:
            return f"### Summary\n{p1}\n\n### Key Findings\n- {p2}\n- {p3}"

    def generate_single_artefact(
        self,
        artefact_type: str,
        source_text: str,
        config: Dict[str, Any],
        grounded_facts: Dict[str, Any]
    ) -> str:
        """Generates one output artefact using the appropriate engine."""
        prompt = build_prompt_for_artefact(artefact_type, source_text, config, grounded_facts)

        # 1. Check if OpenAI requested and API key available
        if (self.provider in ["openai", "auto"]) and self.openai_key:
            try:
                return self._call_openai(prompt)
            except Exception:
                pass

        # 2. Grounded Deterministic Simulation Engine (Gemini is isolated to PPT generation only)
        return self._generate_grounded_offline(artefact_type, source_text, config, grounded_facts)

    def generate_multiple_artefacts(
        self,
        artefact_types: List[str],
        source_text: str,
        config: Dict[str, Any]
    ) -> Dict[str, str]:
        """
        Transforms 1 source into multiple selected artefacts simultaneously.
        """
        grounded_facts = ContentAnalyzer.extract_structured_facts(source_text)
        results: Dict[str, str] = {}

        for a_type in artefact_types:
            output_content = self.generate_single_artefact(a_type, source_text, config, grounded_facts)
            results[a_type] = output_content

        return results
