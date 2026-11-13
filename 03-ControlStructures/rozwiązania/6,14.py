# Zadanie 6.14: Influencer -- co najmniej dwa konta

facebook = True
twitter = False
instagram = True

number_of_accounts = 0

if facebook:
    number_of_accounts += 1
if twitter:
    number_of_accounts += 1
if instagram:
    number_of_accounts += 1

if number_of_accounts >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer")
