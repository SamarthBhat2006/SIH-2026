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
        
        # System / Entity candidates
        potential_systems = []
        for line in lines:
            if any(term in line.lower() for term in ["server", "database", "endpoint", "firewall", "portal", "active directory", "vpn", "cloud", "aws", "azure", "workstation"]):
                potential_systems.append(line[:100])
        potential_systems = potential_systems[:5]

        # Severity indicators mentioned in source
        severity_match = "Not specified in source"
        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL"]:
            if re.search(r"\b" + sev + r"\b", text, re.IGNORECASE):
                severity_match = sev
                break

        return {
            "total_lines": len(lines),
            "detected_dates": detected_dates if detected_dates else ["Not specified in source"],
            "detected_cves": list(set(cve_matches)) if cve_matches else ["Not specified in source"],
            "detected_ips": list(set(ip_matches)) if ip_matches else ["Not specified in source"],
            "detected_domains": list(set(domain_matches)) if domain_matches else ["Not specified in source"],
            "potential_affected_systems": potential_systems if potential_systems else ["Not explicitly enumerated in source"],
            "detected_severity": severity_match,
            "sample_snippet": text[:300] + "..." if len(text) > 300 else text
        }
