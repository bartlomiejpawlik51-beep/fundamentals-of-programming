# 4, Zadanie 2 - Moduł letter_counter
# Polecenie: Zdefiniuj funkcję zliczającą wystąpienia wskazanej litery w tekście.

def count_letter(text, letter):
    """Zwraca liczbę wystąpień podanej litery w tekście."""
    counter = 0
    for character in text:
        if character.lower() == letter.lower():
            counter = counter + 1
    return counter
