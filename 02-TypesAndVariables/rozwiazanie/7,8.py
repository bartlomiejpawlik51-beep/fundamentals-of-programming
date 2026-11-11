import random

dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f'First dice: {dice_roll_1}')
print(f'Second dice: {dice_roll_2}')
print(f'Third dice: {dice_roll_3}')
print(f'Total: {total}')