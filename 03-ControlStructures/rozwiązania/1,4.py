# Zadanie 1.4: Terminal płatniczy

account_balance = 500
total_payment = float(input("Enter total payment: "))

if total_payment <= account_balance:
    print("Payment completed")
    account_balance = account_balance - total_payment
    print("Remaining balance:", account_balance)
else:
    print("No funds")
