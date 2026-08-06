nums = [1,2,2,3,2]

freq = {}

for i in nums:
    freq[i] = freq.get(i,0) + 1

for i in freq:
    if freq[i] > 1:
        print(i)

    