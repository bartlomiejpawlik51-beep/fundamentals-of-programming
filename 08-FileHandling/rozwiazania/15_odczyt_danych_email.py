# ZADANIE 15: Wywołanie funkcji z modułu emails.py.

from emails import sender_email, recipient_email, email_subject, email_body

# Wyświetlamy dane zwrócone przez poszczególne funkcje.
print("Nadawca:", sender_email())
print("Odbiorca:", recipient_email())
print("Temat:", email_subject())
print("Treść wiadomości:")
print(email_body())
