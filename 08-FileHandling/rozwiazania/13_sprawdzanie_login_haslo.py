# ZADANIE 13: Sprawdzenie nazwy użytkownika i hasła za pomocą regex.

import re

username = input("Podaj nazwę użytkownika: ")
password = input("Podaj hasło: ")

# Login musi mieć co najmniej 6 małych liter.
username_pattern = r"^[a-z]{6,}$"

# Hasło musi mieć co najmniej 8 znaków.
# Dozwolone są litery, cyfry i znak podkreślenia.
password_pattern = r"^[A-Za-z0-9_]{8,}$"

# fullmatch sprawdza cały wpisany tekst.
username_match = re.fullmatch(username_pattern, username)
password_match = re.fullmatch(password_pattern, password)

if username_match and password_match:
    print("Nazwa użytkownika i hasło są poprawne.")
else:
    print("Dane nie spełniają wymagań.")

    if not username_match:
        print("Login: minimum 6 małych liter.")

    if not password_match:
        print("Hasło: minimum 8 znaków, tylko litery, cyfry i _.")
