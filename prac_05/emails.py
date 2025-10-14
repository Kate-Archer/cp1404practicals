"""
Prac 05
Email code
1:10 - 1:38
"""


def main():
    """Create dictionary of emails to names."""
    email_to_name = {}
    email = input("What is your email?: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is this your name, {name}? (Y/n)")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name  # add name to email_to_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name}'s email is {email}")


def extract_name_from_email(email):
    """Extract the expected name from provided email address """
    prefix = email.split("@")[0]  # splits at @ in email and returns first part
    parts = prefix.split('.')
    name = " ".join(parts).title()  # returns name with uppercase first letter
    return name


main()
