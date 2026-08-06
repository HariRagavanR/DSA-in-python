arr = [-1,0,10,22,1,33,555,2222]

count = 0

for i in range(len(arr)):
    if arr[i] > 0:
        count = count + 1

print(count)
