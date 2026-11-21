# 4, Zadanie 2
# Polecenie: Policz, ile razy litera e występuje w podanym zdaniu.
# Funkcja zliczająca znajduje się w module letter_counter.py.

import letter_counter

text = "You never get a second chance to make a first impression"
result = letter_counter.count_letter(text, "e")

print(text)
print("The number of letter 'e':", result)
