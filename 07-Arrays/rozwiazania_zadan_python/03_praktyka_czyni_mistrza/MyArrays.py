# 4, Zadanie 20 - Moduł MyArrays
# Polecenie: Moduł zawiera funkcje do wykonywania operacji na listach liczb.
# Funkcje do wykonywania operacji na liście liczb

def second_largest(numbers):
    """Zwraca drugi największy element listy."""
    ordered = numbers.copy()

    # Proste sortowanie bąbelkowe
    for i in range(len(ordered)):
        for j in range(0, len(ordered) - i - 1):
            if ordered[j] > ordered[j + 1]:
                temp = ordered[j]
                ordered[j] = ordered[j + 1]
                ordered[j + 1] = temp

    return ordered[len(ordered) - 2]


def range_difference(numbers):
    """Oblicza różnicę między największą a najmniejszą wartością."""
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    return maximum - minimum


def median(numbers):
    """Sortuje kopię listy i zwraca medianę jej elementów."""
    ordered = numbers.copy()

    for i in range(len(ordered)):
        for j in range(0, len(ordered) - i - 1):
            if ordered[j] > ordered[j + 1]:
                temp = ordered[j]
                ordered[j] = ordered[j + 1]
                ordered[j + 1] = temp

    middle = len(ordered) // 2

    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def smallest_and_largest(numbers):
    """Zwraca listę zawierającą najmniejszą i największą wartość."""
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    return [minimum, maximum]


def numbers_as_string(numbers):
    """Łączy liczby z listy w jeden tekst, oddzielając je myślnikami."""
    result = ""
    for i in range(len(numbers)):
        result = result + str(numbers[i])
        if i < len(numbers) - 1:
            result = result + "-"
    return result
