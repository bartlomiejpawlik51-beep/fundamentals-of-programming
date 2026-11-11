price = input('Enter price: ')
price = float(price)

discount = input('Enter discount %: ')
discount = float(discount)

# Calculate the discount amount
reduction = price * discount / 100

# Calculate the price after discount
new_price = price - reduction

# Display the results
print(f'Price with discount: {new_price:.2f}')
print(f'Reduction: {reduction:.2f}')