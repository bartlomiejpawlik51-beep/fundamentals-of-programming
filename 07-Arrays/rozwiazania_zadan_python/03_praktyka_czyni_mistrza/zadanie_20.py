# 4, Zadanie 20 - Praktyka czyni mistrza
# Polecenie: Utwórz moduł MyArrays z funkcjami do obliczania drugiej największej liczby, rozstępu, mediany, minimum i maksimum oraz tekstowej postaci listy.
# Program korzystający z modułu MyArrays
# Uruchom ten plik razem z plikiem MyArrays.py w tym samym folderze.

import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ",".join(str(number) for number in numbers))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Difference:", MyArrays.range_difference(numbers))
print("Median:", MyArrays.median(numbers))

smallest_largest = MyArrays.smallest_and_largest(numbers)
print("Smallest and largest number:", str(smallest_largest[0]) + "," + str(smallest_largest[1]))

print("Numbers as a string:", MyArrays.numbers_as_string(numbers))
