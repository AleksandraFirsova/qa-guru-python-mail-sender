from datetime import date


def normalize_addresses(value: str) -> str:
    return value.lower().strip()


def add_short_body(email: dict) -> dict:
    body = email.get("body", "")
    email["short_body"] = body[:10] + "..."
    return email


def clean_body_text(body: str) -> str:
    return body.replace("\t", " ").replace("\n", " ").strip()


def build_sent_text(email: dict) -> str:
    body = email.get("body", "")

    return (
        f"Кому: {email['recipient']}, от {email['sender']}\n"
        f"Тема: {email['subject']}, дата {email['date']}\n"
        f"{body}"
    )


def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    is_subject_empty = not subject.strip()
    is_body_empty = not body.strip()
    return (is_subject_empty, is_body_empty)


def mask_sender_email(login: str, domain: str) -> str:
    return login[:2] + "***@" + domain


def get_correct_email(email_list: list[str]) -> list[str]:
    correct_emails = []
    for email in email_list:
        clean_email = email.strip()
        if "@" in clean_email and clean_email.lower().endswith((".com", ".ru", ".net")):
            correct_emails.append(clean_email)
    return correct_emails


test_emails = [
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]


def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    return {"sender": sender, "recipient": recipient, "subject": subject, "body": body}


def add_send_date(email: dict) -> dict:
    today = date.today().isoformat()
    email["date"] = today
    return email


def extract_login_domain(address: str) -> tuple[str, str]:
    parts = address.split("@", 1)
    if len(parts) == 2:
        login, domain = parts
        return login, domain

    return "", ""