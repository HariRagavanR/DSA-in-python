prices = [7, 1, 5, 3, 6, 4]

minimum = float('inf')

profit = 0

for price in prices:

    minimum = min(minimum,price)

    profit = max(profit, price - minimum)

print(profit)