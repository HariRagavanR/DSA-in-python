arr = [10,22,1,33,555,2222]
old = 22
new = 122
for i in range(len(arr)):
    if arr[i] == old:
        arr[i] = new
        
print([new])
