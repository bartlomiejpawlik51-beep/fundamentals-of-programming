# Zadanie 6.10: Wiek psa w psich latach

human_age = int(input("Enter dog's age in human years: "))

if human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = 2 * 10.5 + (human_age - 2) * 4

print("Dog's age in dog years is:", dog_age)
