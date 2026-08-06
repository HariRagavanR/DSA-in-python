arr = [10,22,1,33,555,2222]

target = 33

last = -1

for i in range(len(arr)):
    if arr[i] == target:
        last = i

print(last)