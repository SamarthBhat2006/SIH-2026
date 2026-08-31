"""
Security & Threat Screening Module
Performs heuristic prompt injection detection and sensitive data pattern matching.
"""

import re
from typing import Dict, List, Any
from config.settings import (
    SENSITIVE_PATTERNS,
    PROMPT_INJECTION_PATTERNS,
    STRICT_INJECTION_BLOCKING,
    ENABLE_SENSITIVE_DATA_MASKING,
)

REDACTION_TAGS = {
    "Email Address": "[REDACTED_EMAIL]",
    "IPv4 Address": "[REDACTED_IP_ADDRESS]",
    "API Key / Secret Token": "[REDACTED_SECRET_TOKEN]",
    "Generic Key String": "[REDACTED_API_KEY]",
    "Password Assignment": "[REDACTED_PASSWORD]",
    "Phone Number": "[REDACTED_PHONE_NUMBER]",
}

class SecurityScanner:
    """Security engine for analyzing untrusted user input and enforcing safety policies."""

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

        if has_injection:
            if STRICT_INJECTION_BLOCKING:
                mitigation_note = (
                    "🛑 STRICT POLICY ACTIVE: Input contains prompt injection signatures and transformation "
                    "will be strictly blocked."
                )
            else:
                mitigation_note = (
                    "Untrusted input isolated: Content will be processed strictly as passive data "
                    "tokens and wrapped with immutable system guardrails."
                )
        else:
            mitigation_note = "No adversarial prompt manipulation patterns detected."

        return {
            "has_injection_risk": has_injection,
            "risk_level": risk_level,
            "detected_count": len(detected_signatures),
            "signatures": detected_signatures,
            "strict_blocking_enabled": STRICT_INJECTION_BLOCKING,
            "mitigation_note": mitigation_note,
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

        if has_sensitive:
            if ENABLE_SENSITIVE_DATA_MASKING:
                advisory_note = (
                    f"🔒 AUTOMATIC MASKING ENABLED: {total_findings} sensitive item(s) detected. "
                    "All sensitive values will be redacted with safe placeholder tokens prior to AI transformation."
                )
            else:
                advisory_note = (
                    "Sensitive information pattern detected (e.g. IPs, emails, or token-like strings). "
                    "Ensure source authorization before multi-channel dissemination."
                )
        else:
            advisory_note = "No sensitive credentials or anomalous tokens detected."

        return {
            "has_sensitive_data": has_sensitive,
            "total_sensitive_items": total_findings,
            "findings_by_category": findings,
            "masking_enabled": ENABLE_SENSITIVE_DATA_MASKING,
            "advisory_note": advisory_note,
        }

    @classmethod
    def mask_sensitive_data(cls, text: str) -> str:
        """
        Replaces detected sensitive tokens (emails, IPs, API keys, passwords, generic keys, phone numbers)
        with safe placeholder tags (e.g. [REDACTED_EMAIL], [REDACTED_IP_ADDRESS]).
        """
        if not text:
            return text

        masked = text
        for label, pattern_str in SENSITIVE_PATTERNS.items():
            tag = REDACTION_TAGS.get(label, f"[REDACTED_{label.upper().replace(' ', '_')}]")
            compiled = re.compile(pattern_str)
            if compiled.groups > 0:
                def _replace_group(match, placeholder=tag):
                    if match.lastindex and match.group(1):
                        start = match.start(1) - match.start(0)
                        end = match.end(1) - match.start(0)
                        orig = match.group(0)
                        return orig[:start] + placeholder + orig[end:]
                    return placeholder
                masked = compiled.sub(_replace_group, masked)
            else:
                masked = compiled.sub(tag, masked)

        return masked

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
            "strict_blocking_enabled": STRICT_INJECTION_BLOCKING,
            "masking_enabled": ENABLE_SENSITIVE_DATA_MASKING,
            "scanned_char_count": len(text),
        }
