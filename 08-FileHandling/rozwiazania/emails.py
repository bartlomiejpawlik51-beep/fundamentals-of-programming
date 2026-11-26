# MODUŁ emails.py: funkcje pobierające informacje z pliku email.txt.

import re


def sender_email(file_name="email.txt"):
    """Zwraca adres e-mail nadawcy z nagłówka From."""
    with open(file_name, "r", encoding="utf-8") as file:
        email_text = file.read()

    result = re.search(
        r"^From:.*?<([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})>",
        email_text,
        re.MULTILINE
    )

    if result:
        return result.group(1)
    return "Nie znaleziono adresu nadawcy"


def recipient_email(file_name="email.txt"):
    """Zwraca adres e-mail odbiorcy z nagłówka To."""
    with open(file_name, "r", encoding="utf-8") as file:
        email_text = file.read()

    result = re.search(
        r"^To:.*?<([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})>",
        email_text,
        re.MULTILINE
    )

    if result:
        return result.group(1)
    return "Nie znaleziono adresu odbiorcy"


def email_subject(file_name="email.txt"):
    """Zwraca temat wiadomości z nagłówka Subject."""
    with open(file_name, "r", encoding="utf-8") as file:
        email_text = file.read()

    result = re.search(r"^Subject:\s*(.*)", email_text, re.MULTILINE)

    if result:
        return result.group(1).strip()
    return "Nie znaleziono tematu"


def email_body(file_name="email.txt"):
    """Zwraca treść wiadomości znajdującą się po pustym wierszu."""
    with open(file_name, "r", encoding="utf-8") as file:
        email_text = file.read()

    # Dzielimy nagłówki i treść wiadomości.
    parts = re.split(r"\r?\n\r?\n", email_text, maxsplit=1)

    if len(parts) == 2:
        return parts[1].strip()
    return "Nie znaleziono treści wiadomości"
