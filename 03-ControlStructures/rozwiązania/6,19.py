# Zadanie 6.19: Ankieta -- trzy pytania

print("SURVEY")
answer1 = input("Are you interested in computer science? (t/n): ").lower() == "t"
answer2 = input("Do you like playing computer games? (t/n): ").lower() == "t"
answer3 = input("Do you have an Instagram account? (t/n): ").lower() == "t"

print("\nSURVEY RESULTS")
if answer1:
    print("Interest in computer science: Yes")
else:
    print("Interest in computer science: No")

if answer2:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if answer3:
    print("Having an Instagram account: Yes")
else:
    print("Having an Instagram account: No")
