arr = [111,22,111,33,555,2222]

result = []

for i in arr:
    if i not in result:
        result.append(i)

print(result)