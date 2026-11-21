# 4, Zadanie 10 - Moduł keyboard
# Polecenie: Zdefiniuj funkcje do odczytywania tekstu, liczby całkowitej,
# liczby rzeczywistej i wartości logicznej z klawiatury.

def input_string(message):
    """Pobiera tekst wpisany przez użytkownika."""
    value = input(message)
    return value

def input_integer(message):
    """Pobiera tekst i zamienia go na liczbę całkowitą."""
    value = int(input(message))
    return value

def input_real(message):
    """Pobiera tekst i zamienia go na liczbę rzeczywistą."""
    value = float(input(message))
    return value

def input_boolean(message):
    """Pobiera odpowiedź y/n i zwraca True dla y oraz False dla n."""
    answer = input(message).lower()
    return answer == "y"
