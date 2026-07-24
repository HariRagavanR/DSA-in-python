arr = [1,3,5,7,9,20,22,1,33,555,2222]

# Formula : Not Divisible by 2, remainder is 1

odd_count = 0

for i in arr:
    if i % 2 != 0:

        odd_count = odd_count + 1

print([odd_count])

