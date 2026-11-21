# 4, Zadanie 5
# Polecenie: Zdefiniuj funkcję, która na podstawie liczby punktów zwraca ocenę końcową.

def pts_to_grade(points):
    """Zwraca ocenę słowną na podstawie liczby zdobytych punktów."""
    if points >= 18:
        grade = "Doskonały"
    elif points >= 14:
        grade = "Dobry"
    elif points >= 10:
        grade = "Dostateczny"
    else:
        grade = "Niedostateczny"

    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print("Liczba punktów:", test_result)
print("Ocena końcowa:", final_grade)
