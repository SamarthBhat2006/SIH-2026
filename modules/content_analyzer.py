"""
Content Analyzer & Anti-Hallucination Grounding Module
Extracts structured facts, entities, and contextual signals from the source document.
"""

import re
from typing import Dict, List, Any

class ContentAnalyzer:
    """Extracts structured entities, timelines, and facts from source text."""

    @staticmethod
    def extract_structured_facts(text: str) -> Dict[str, Any]:
        """
        Parses the text to identify core factual anchors so generation is grounded.
        """
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        
        # Extract title or reference ID
        doc_title = "Operational Intelligence Report"
        ref_id_matches = re.findall(r"\b(?:IR|INC|ADV|NTRO|ALERT|REP|VULN|SEC)-[A-Z0-9-]+\b", text, re.IGNORECASE)
        ref_id = ref_id_matches[0] if ref_id_matches else "NTRO-OP-2026"
        
        for line in lines[:4]:
            clean_l = re.sub(r"^[#*_\-\s:]+", "", line).strip()
            if len(clean_l) > 6 and not any(term in clean_l.lower() for term in ["date:", "severity:", "author:"]):
                doc_title = clean_l[:80]
                break

        # Extract potential dates / timestamps
        date_patterns = [
            r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4}\b",
            r"\b\d{4}-\d{2}-\d{2}\b",
            r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
            r"\b\d{1,2}:\d{2}(?::\d{2})?\s*(?:UTC|GMT|EST|PST|IST)?\b"
        ]
        detected_dates: List[str] = []
        for pat in date_patterns:
            detected_dates.extend(re.findall(pat, text, re.IGNORECASE))
        detected_dates = list(dict.fromkeys(detected_dates))[:8]

        # Extract indicators / IOCs (IPs, domains, hashes, CVEs)
        cve_matches = re.findall(r"\bCVE-\d{4}-\d{4,7}\b", text, re.IGNORECASE)
        ip_matches = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", text)
        domain_matches = re.findall(r"\b(?:[a-zA-Z0-9-]+\.)+(?:com|org|net|gov|in|io|xyz|ru|cn|info)\b", text)
        hash_matches = re.findall(r"\b[a-fA-F0-9]{64}\b", text)
        
        # System / Entity candidates
        potential_systems = []
        impacted_users = []
        mitigations = []
        attack_vectors = []

        for line in lines:
            ll = line.lower()
            if any(term in ll for term in ["server", "database", "endpoint", "firewall", "portal", "active directory", "vpn", "cloud", "aws", "azure", "workstation", "gateway"]):
                potential_systems.append(line.lstrip("-*# ").strip())
            if any(term in ll for term in ["personnel", "user", "admin", "employee", "staff", "account", "credentials"]):
                impacted_users.append(line.lstrip("-*# ").strip())
            if any(term in ll for term in ["mitigat", "remediat", "action", "revok", "patch", "enforce", "block", "isolate", "isolate", "rotate"]):
                mitigations.append(line.lstrip("-*# ").strip())
            if any(term in ll for term in ["phish", "exploit", "zero-day", "brute force", "malware", "ransomware", "injection", "lure", "harvest", "vulnerability"]):
                attack_vectors.append(line.lstrip("-*# ").strip())

        # Deduplicate & slice
        potential_systems = list(dict.fromkeys(potential_systems))[:4]
        impacted_users = list(dict.fromkeys(impacted_users))[:3]
        mitigations = list(dict.fromkeys(mitigations))[:4]
        attack_vectors = list(dict.fromkeys(attack_vectors))[:3]

        # Severity indicators mentioned in source
        severity_match = "Not specified in source material."
        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL"]:
            if re.search(r"\b" + sev + r"\b", text, re.IGNORECASE):
                severity_match = sev
                break

        return {
            "title": doc_title,
            "ref_id": ref_id,
            "total_lines": len(lines),
            "detected_dates": detected_dates if detected_dates else ["Not specified in source material."],
            "detected_cves": list(set(cve_matches)) if cve_matches else ["Not specified in source material."],
            "detected_ips": list(set(ip_matches)) if ip_matches else ["Not specified in source material."],
            "detected_domains": list(set(domain_matches)) if domain_matches else ["Not specified in source material."],
            "detected_hashes": list(set(hash_matches)) if hash_matches else ["Not specified in source material."],
            "potential_affected_systems": potential_systems if potential_systems else ["Not specified in source material."],
            "impacted_users": impacted_users if impacted_users else ["Not specified in source material."],
            "mitigations": mitigations if mitigations else ["Not specified in source material."],
            "attack_vectors": attack_vectors if attack_vectors else ["Not specified in source material."],
            "detected_severity": severity_match,
            "sample_snippet": text[:300] + "..." if len(text) > 300 else text
        }

