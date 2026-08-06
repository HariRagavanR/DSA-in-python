arr = [4, 6, 99, 3, 7]

for i in range(len(arr)):

    left = sum(arr[:i])
    right = sum(arr[i+1:])

    if left == right:
        print(i)
