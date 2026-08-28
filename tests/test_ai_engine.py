"""
Unit tests for the AI transformation engine and grounded prompt generator.
"""

from modules.ai_engine import AIEngine
from modules.content_analyzer import ContentAnalyzer

SAMPLE_TEXT = """
INCIDENT RESPONSE REPORT: IR-2026-0884
NATIONAL CYBER OPERATIONS CENTER (NCOC) / NTRO
DATE: 2026-08-28 14:30:00 UTC
SEVERITY: HIGH

1. EXECUTIVE OVERVIEW
The SOC identified a credential harvesting phishing campaign targeting engineering personnel.
Lures redirected users to counterfeit portal at 198.51.100.42 and domain verify-secops-ntro.org.

2. IMPACT & MITIGATIONS
- Affected Systems: Exchange Online Mail Gateway and Azure AD Endpoint Auth.
- Mitigations: Revoked active sessions and enforced FIDO2 tokens.
"""

def test_content_analyzer_grounding():
    facts = ContentAnalyzer.extract_structured_facts(SAMPLE_TEXT)
    assert facts["detected_severity"] == "HIGH"
    assert any("198.51.100.42" in ip for ip in facts["detected_ips"])
    assert any("verify-secops-ntro.org" in d for d in facts["detected_domains"])

def test_ai_engine_offline_multi_generation():
    engine = AIEngine(provider="offline_simulation")
    selected_outputs = [
        "executive_summary",
        "cybersecurity_advisory",
        "linkedin_post",
        "x_thread",
        "presentation"
    ]
    config = {
        "audience": "Executive",
        "tone": "Professional",
        "detail": "Standard",
        "objective": "Inform"
    }

    results = engine.generate_multiple_artefacts(selected_outputs, SAMPLE_TEXT, config)

    assert len(results) == 5
    assert "executive_summary" in results
    assert "Executive" in results["executive_summary"] or "Situation Overview" in results["executive_summary"]
    assert "cybersecurity_advisory" in results
    assert "Indicators of Compromise" in results["cybersecurity_advisory"]
    assert "linkedin_post" in results
    assert "#CyberSecurity" in results["linkedin_post"]
    assert "x_thread" in results
    assert "🧵" in results["x_thread"]
    assert "presentation" in results
    assert "SLIDE 1" in results["presentation"]
