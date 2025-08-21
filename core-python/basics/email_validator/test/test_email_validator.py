import pytest
from module.email_validator import is_valid_email, extract_domain, generate_report

def test_is_valid_email() -> None:
    """Test email validation function."""
    assert is_valid_email("alice@gmail.com") is True, "Valid email should return True"
    assert is_valid_email("invalid.email") is False, "Missing '@' should return False"
    assert is_valid_email("no@domain") is False, "Missing domain part should return False"
    assert is_valid_email("") is False, "Empty email should return False"

def test_extract_domain() -> None:
    """Test domain extraction from emails."""
    assert extract_domain("alice@gmail.com") == "gmail.com", "Should extract correct domain"
    assert extract_domain("invalid.email") == "", "Invalid email should return empty string"
    assert extract_domain("no@domain") == "", "Invalid domain should return empty string"

def test_generate_report() -> None:
    """Test report generation with various inputs."""
    emails: list[str] = [
        "alice@gmail.com",
        "bob@work.com",
        "invalid.email",
        "charlie.personal@yahoo.com"
    ]
    
    # Test: All valid emails
    report = generate_report(emails)
    expected = {
        "gmail.com": ["alice@gmail.com"],
        "work.com": ["bob@work.com"],
        "yahoo.com": ["charlie.personal@yahoo.com"]
    }
    assert report == expected, "Report should group valid emails by domain"

    # Test: Filter by category
    report = generate_report(emails, "personal")
    expected = {"yahoo.com": ["charlie.personal@yahoo.com"]}
    assert report == expected, "Report should filter by category"

    # Test: Include invalid emails
    report = generate_report(emails, show_invalid=True)
    expected = {
        "gmail.com": ["alice@gmail.com"],
        "work.com": ["bob@work.com"],
        "yahoo.com": ["charlie.personal@yahoo.com"],
        "invalid": ["invalid.email"]
    }
    assert report == expected, "Report should include invalid emails when requested"

    # Test: Empty email list
    report = generate_report([])
    assert report == {}, "Empty email list should return empty report"

def test_generate_report_edge_cases() -> None:
    """Test edge cases for generate_report."""
    # Test: Single invalid email
    report = generate_report(["invalid.email"], show_invalid=True)
    assert report == {"invalid": ["invalid.email"]}, "Should handle single invalid email"
    
    # Test: No matching category
    report = generate_report(["alice@gmail.com"], "work")
    assert report == {}, "No matching emails should return empty report"
