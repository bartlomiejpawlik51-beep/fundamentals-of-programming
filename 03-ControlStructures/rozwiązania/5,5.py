# Zadanie 5.5: Suma i średnia liczb do momentu wpisania zera

total_sum = 0
counter = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break  # break natychmiast kończy pętlę

    total_sum += number
    counter += 1

print("The total sum of the numbers is:", total_sum)

if counter > 0:
    average = total_sum / counter
    print("The average is:", average)
else:
    print("No numbers were entered")
