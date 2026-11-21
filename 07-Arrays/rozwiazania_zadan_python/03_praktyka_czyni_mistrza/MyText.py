# 4, Zadanie 25 - Moduł MyText
# Polecenie: Moduł zawiera funkcje do analizy i sortowania słów w tekście.
# Funkcje do pracy z tekstem

def number_of_words(text):
    """Zwraca liczbę słów znajdujących się w tekście."""
    words = text.split()
    return len(words)


def words_by_length(text):
    """Zwraca słowa posortowane od najdłuższego do najkrótszego."""
    words = text.split()
    words.sort(key=len, reverse=True)
    return words


def words_alphabetically(text):
    """Zwraca słowa posortowane alfabetycznie."""
    words = text.split()
    words.sort()
    return words
