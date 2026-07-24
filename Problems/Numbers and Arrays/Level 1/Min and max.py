arr = [1, 4, 3, 5, 4, 8, 6]

minimum = maximum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i

print([minimum,maximum])