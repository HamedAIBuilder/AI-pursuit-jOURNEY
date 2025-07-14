import re

def validate_email(email):
    """
    Validate an email address using a regular expression.
    Returns True if the email is valid, False otherwise.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    # Example usage
    test_emails = [
        "user@example.com",
        "user.name@domain.co",
        "invalid-email@",
        "another.user@domain",
        "user@domain.com"
    ]
    for email in test_emails:
        print(f"{email}: {validate_email(email)}") 