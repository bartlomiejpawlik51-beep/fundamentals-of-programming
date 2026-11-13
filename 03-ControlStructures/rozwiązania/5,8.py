# Zadanie 5.8: Bankomat -- wpłata, wypłata, saldo, PIN i zmiana PIN-u

balance = 1000.0
pin = "1234"
entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    while True:
        print("\n1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Change PIN")
        print("5 - Exit")
        choice = input("Choose option: ")

        if choice == "1":
            print("Balance:", balance)
        elif choice == "2":
            amount = float(input("Deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit completed")
            else:
                print("Incorrect amount")
        elif choice == "3":
            amount = float(input("Withdraw amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print("Withdrawal completed")
            else:
                print("Not enough funds or incorrect amount")
        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            if old_pin == pin:
                new_pin = input("Enter new 4-digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():  # isdigit() sprawdza, czy tekst zawiera same cyfry
                    pin = new_pin
                    print("PIN changed")
                else:
                    print("PIN must contain exactly 4 digits")
            else:
                print("Incorrect current PIN")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Incorrect option")
else:
    print("Incorrect PIN")
