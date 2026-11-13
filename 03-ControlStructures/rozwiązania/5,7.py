# Zadanie 5.7: Timer -- ostatnie pięć sekund słownie

number = int(input("Enter number of seconds: "))
words = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć"]

while number > 0:
    if number <= 5:
        print(words[number])
    else:
        print(number)
    number -= 1
