import random

# COMPUTER TURN
computer = random.randint(1, 6)

# YOUR TURN
you = int(input('Guess the number from 1 to 6: '))

# Check the result
result = computer == you

print(f'Computer rolled: {computer}')
print(f'You won: {result}')