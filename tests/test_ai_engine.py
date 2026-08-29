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
    assert "Not specified in source material." in facts["detected_cves"]

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

    # 1. Executive Summary checks
    exec_sum = results["executive_summary"]
    assert "EXECUTIVE SUMMARY" in exec_sum
    assert "Situation / Context" in exec_sum
    assert "Key Findings" in exec_sum
    assert "Recommended Actions" in exec_sum
    assert "Conclusion" in exec_sum

    # 2. Cybersecurity Advisory checks
    adv = results["cybersecurity_advisory"]
    assert "CYBERSECURITY ADVISORY" in adv
    assert "Severity:" in adv
    assert "Threat Overview" in adv
    assert "Indicators of Compromise" in adv
    assert "198.51.100.42" in adv
    assert "Recommended Mitigation" in adv
    assert "Incident Response Recommendations" in adv

    # 3. LinkedIn Post checks
    li = results["linkedin_post"]
    assert "#CyberSecurity" in li
    assert "Key Takeaway" in li or "💡" in li

    # 4. X / Twitter Thread checks
    x_th = results["x_thread"]
    assert "1/" in x_th
    assert "2/" in x_th
    assert "3/" in x_th
    assert "4/" in x_th
    assert "5/" in x_th

    # 5. Presentation Deck checks
    pres = results["presentation"]
    assert "SLIDE 1 — TITLE" in pres
    assert "SLIDE 2 — OVERVIEW" in pres
    assert "SLIDE 3 — KEY FINDINGS" in pres
    assert "SLIDE 4 — IMPACT / RISK" in pres
    assert "SLIDE 5 — RECOMMENDATIONS" in pres
    assert "SLIDE 6 — CONCLUSION" in pres
    assert "Speaker Notes:" in pres

def test_configuration_influence():
    engine = AIEngine(provider="offline_simulation")
    grounded_facts = ContentAnalyzer.extract_structured_facts(SAMPLE_TEXT)

    # Test Urgent vs Professional Tone
    urgent_out = engine.generate_single_artefact(
        "executive_summary",
        SAMPLE_TEXT,
        {"audience": "Executive", "tone": "Urgent", "detail": "Detailed", "objective": "Alert"},
        grounded_facts
    )
    assert "URGENT ACTION REQUIRED" in urgent_out or "Immediate" in urgent_out

