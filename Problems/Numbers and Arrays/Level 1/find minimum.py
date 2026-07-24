arr = [10,22,-1,33,555,2222]

minimum = arr[0]

for i in arr:
    if i < minimum:
        minimum = i

print(minimum)