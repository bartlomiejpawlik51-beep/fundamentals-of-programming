# 4, Zadanie 25 - Praktyka czyni mistrza
# Polecenie: Utwórz moduł MyText z funkcjami zliczającymi słowa oraz sortującymi je według długości i alfabetycznie.
# Program korzystający z modułu MyText
# Uruchom ten plik razem z plikiem MyText.py w tym samym folderze.

import MyText

text = "Jedno jabłko dziennie trzyma lekarza z daleka"

print("Text:", text)
print("Number of words:", MyText.number_of_words(text))
print("Words from the longest:", ", ".join(MyText.words_by_length(text)))
print("Words ordered alphabetically:", ", ".join(MyText.words_alphabetically(text)))
