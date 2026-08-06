arr = [100,22,111,33,555,2222]

smallest = float('inf')
second = float('inf')

for i in arr:
    if i < smallest:
        second = smallest
        smallest = i
    elif i < second and i != smallest:
        second = i

print(second)
