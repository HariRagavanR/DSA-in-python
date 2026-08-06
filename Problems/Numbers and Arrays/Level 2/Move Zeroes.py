arr = [0,10,22,1,0,33,0,0,0,555,2222,0]

result = []

for i in arr:

    if i != 0:
        result.append(i)

while(len(result)) < len(arr):
    result.append(0)

print(result)