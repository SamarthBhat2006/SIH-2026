"""
Security & Threat Screening Module
Performs heuristic prompt injection detection and sensitive data pattern matching.
"""

import re
from typing import Dict, List, Any
from config.settings import SENSITIVE_PATTERNS, PROMPT_INJECTION_PATTERNS

class SecurityScanner:
    """Security engine for analyzing untrusted user input."""

    @classmethod
    def detect_prompt_injections(cls, text: str) -> Dict[str, Any]:
        """
        Scans text for adversarial prompt injection cues, jailbreak patterns,
        and system role override attempts.
        """
        detected_signatures: List[Dict[str, str]] = []
        
        for pattern_str in PROMPT_INJECTION_PATTERNS:
            matches = list(re.finditer(pattern_str, text, re.IGNORECASE))
            for match in matches:
                detected_signatures.append({
                    "pattern": pattern_str,
                    "matched_text": match.group(0),
                    "start": match.start(),
                    "end": match.end(),
                })

        has_injection = len(detected_signatures) > 0
        risk_level = "HIGH" if len(detected_signatures) >= 2 else ("MEDIUM" if has_injection else "LOW")

        return {
            "has_injection_risk": has_injection,
            "risk_level": risk_level,
            "detected_count": len(detected_signatures),
            "signatures": detected_signatures,
            "mitigation_note": (
                "Untrusted input isolated: Content will be processed strictly as passive data "
                "tokens and wrapped with immutable system guardrails."
                if has_injection else "No adversarial prompt manipulation patterns detected."
            )
        }

    @classmethod
    def detect_sensitive_data(cls, text: str) -> Dict[str, Any]:
        """
        Scans text for sensitive data patterns like emails, IP addresses,
        API keys, authentication tokens, and credentials.
        """
        findings: Dict[str, List[str]] = {}
        total_findings = 0

        for label, pattern_str in SENSITIVE_PATTERNS.items():
            matches = re.findall(pattern_str, text)
            if matches:
                # Deduplicate while preserving order
                unique_matches = list(dict.fromkeys(matches))[:10] # limit to 10 for display
                findings[label] = unique_matches
                total_findings += len(matches)

        has_sensitive = total_findings > 0

        return {
            "has_sensitive_data": has_sensitive,
            "total_sensitive_items": total_findings,
            "findings_by_category": findings,
            "advisory_note": (
                "Sensitive information pattern detected (e.g. IPs, emails, or token-like strings). "
                "Ensure source authorization before multi-channel dissemination."
                if has_sensitive else "No sensitive credentials or anomalous tokens detected."
            )
        }

    @classmethod
    def full_scan(cls, text: str) -> Dict[str, Any]:
        """Runs the complete security screening suite."""
        injection_report = cls.detect_prompt_injections(text)
        sensitive_report = cls.detect_sensitive_data(text)

        overall_status = "CLEAN"
        if injection_report["has_injection_risk"] and sensitive_report["has_sensitive_data"]:
            overall_status = "WARNING_INJECTION_AND_SENSITIVE"
        elif injection_report["has_injection_risk"]:
            overall_status = "WARNING_INJECTION"
        elif sensitive_report["has_sensitive_data"]:
            overall_status = "NOTICE_SENSITIVE_DATA"

        return {
            "overall_status": overall_status,
            "injection_report": injection_report,
            "sensitive_report": sensitive_report,
            "scanned_char_count": len(text),
        }
