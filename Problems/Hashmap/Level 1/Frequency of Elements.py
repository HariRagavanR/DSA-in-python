nums = [1,2,2,3,1,2]

freq = {}

for i in nums:

    freq[i] = freq.get(i,0) + 1

print(freq)

