# Zadanie 6.16: Czas prania

total_washing_time = 0
program = input("Select washing program: (j)acket, (u)nderwear, (s)hoes: ")
extra_rinse = input("Extra rinse? (y/n): ")
extra_spin = input("Extra spin? (y/n): ")

if program == "j":
    total_washing_time = 40
elif program == "u":
    total_washing_time = 70
elif program == "s":
    total_washing_time = 20
else:
    print("Incorrect program")

if extra_rinse == "y":
    total_washing_time += 15
if extra_spin == "y":
    total_washing_time += 9

print("Total washing time:", total_washing_time, "minutes")
