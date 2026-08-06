arr = [10,22,111,33,555,2222]

largest = float('-inf')
second = float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i != largest:
        second = i

print(second)

