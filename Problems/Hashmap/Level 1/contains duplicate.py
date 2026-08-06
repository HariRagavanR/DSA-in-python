nums = [1,2,2,3,4]

seen = set()

for i in nums:
    if i in seen:
        print(True)

    seen.add(i)

