arr = [111, 111, 111, 33, 555, 111]

for i in arr:
    count = 0

    for j in arr:
        if j == i:
            count = count + 1

    if count > len(arr) // 2:
        print(i)