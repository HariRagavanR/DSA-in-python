nums = [4,3,2,7,8,2,3,1]

def find_duplicates(nums):

    freq = {}

    for i in nums:
        freq[i] = freq.get(i,0) +1

    result = []

    for i in freq:
        if freq[i] == 2:
            result.append(i)

    return result

print(find_duplicates(nums))

