# 4, Zadanie 12 - Praktyka czyni mistrza
# Polecenie: Napisz program, który wyświetla elementy pierwszej listy, których nie ma w drugiej liście.
# Liczby z pierwszej listy, których nie ma w drugiej

arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

print("Liczby występujące tylko w pierwszej liście:")
for number in arr1:
    if number not in arr2:
        print(number)
