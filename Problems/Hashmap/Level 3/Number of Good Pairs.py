nums = [1,2,3,1,1,3]

def num_iden_pairs(nums):
    freq = {}

    pairs = 0

    for num in nums:
        if num in freq:
            pairs += freq[num]

        freq[num] = freq.get(num,0) + 1

    return pairs

print(num_iden_pairs(nums))


