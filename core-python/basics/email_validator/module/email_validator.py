def is_valid_email(email: str) -> bool:
    """Return True if email has '@' and a domain, False otherwise"""
    try:
        if "@" in email and "." in email.split("@")[1]:
            return True
        return False
    except IndexError:
        return False


def extract_domain(email: str) -> str:
    """Extract the domain from a valid email"""
    return email.split("@")[1] if is_valid_email(email) else ""


def generate_report(
    emails: list[str], *categories: str, **options: bool
) -> dict[str, list[str]]:
    """Groups valid emails by domain, optionally filtering by category"""

    report: dict[str, list[str]] = {}
    show_invalid: bool = options.get("show_invalid", False)

    for email in emails:
        if is_valid_email(email):
            domain = extract_domain(email)
            # Check if email matches any category (e.g., 'personal', 'work')
            matches_category = any(
                category.lower() in email.lower() for category in categories
            )
            if not categories or matches_category:
                if domain not in report:
                    report[domain] = []
                report[domain].append(email)
        elif show_invalid:
            if "invalid" not in report:
                report["invalid"] = []
            report["invalid"].append(email)
    return report


def print_report(report: dict[str, list[str]]) -> None:
    """Displays emails grouped by domain"""

    if not report:
        print("No emails to report")
        return
    for domain, emails in report.items():
        print(f"\nDomain: {domain}")
        for email in emails:
            print(f"  - {email}")
