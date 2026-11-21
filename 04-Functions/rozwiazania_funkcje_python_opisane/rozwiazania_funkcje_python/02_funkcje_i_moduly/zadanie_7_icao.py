# 4, Zadanie 7
# Polecenie: Użyj alfabetu fonetycznego ICAO, aby przeliterować słowo wpisane z klawiatury.

def icao_word(letter):
    """Zwraca słowo alfabetu ICAO odpowiadające podanej literze."""
    alphabet = {
        "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta",
        "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
        "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima",
        "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
        "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
        "Y": "Yankee", "Z": "Zulu"
    }

    letter = letter.upper()
    if letter in alphabet:
        return alphabet[letter]
    return letter

name = input("Wpisz nazwę: ")
print("Literowanie:")
for letter in name:
    if letter.isalpha():
        print(icao_word(letter))
    elif letter == " ":
        print("Przerwa")
    else:
        print(letter)
