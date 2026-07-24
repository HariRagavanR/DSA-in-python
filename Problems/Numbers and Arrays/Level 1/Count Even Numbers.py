arr = [10,22,1,33,555,2222]

# Formula : Divisible by 2, remainder is 0

even_count = 0

for i in arr:
    if i % 2 == 0:
        even_count = even_count + 1

print([even_count])