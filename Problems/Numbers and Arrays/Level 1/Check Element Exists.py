arr = [10,22,1,33,555,2222]

target = 555

for i in arr:
    if i == target:
        print(target)
        break
else:
    print("Target was not found in the array")