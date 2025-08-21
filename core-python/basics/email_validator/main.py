"""Email Validator"""

from module.email_validator import generate_report, print_report

def main() -> None:
    """Main program"""

    emails: list[str] = [
        "alice@gmail.com",
        "bob@work.com",
        "invalid.email",
        "charlie.personal@yahoo.com",
        "dave@outlook.com",
    ]

    # Generate reports with different options
    print("Report 1: All valid emails")
    report1 = generate_report(emails)
    print_report(report1)

    print("\nReport 2: Personal emails only")
    report2 = generate_report(emails, "personal")
    print_report(report2)

    print("\nReport 3: All emails (including invalid)")
    report3 = generate_report(emails, show_invalid=True)
    print_report(report3)


if __name__ == "__main__":
    main()
