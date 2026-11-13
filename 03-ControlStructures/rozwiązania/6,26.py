# Zadanie 6.26: PIN z trzema próbami

correct_pin = "0805"
attempts = 0
logged_in = False

while attempts < 3:
    entered_pin = input("Enter PIN: ")

    if entered_pin == correct_pin:
        print("Correct PIN")
        logged_in = True
        break
    else:
        print("Incorrect PIN...")
        attempts += 1

if not logged_in:
    print("Unfortunately, your payment card has been blocked.")
