arr = [10,22,111,33,555,2222]

smallest = None

for i in arr:

    if i % 2 != 0:
        if smallest is None or i < smallest:
            smallest = i

print(smallest)