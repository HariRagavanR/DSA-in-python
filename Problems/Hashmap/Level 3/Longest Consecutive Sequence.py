nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
def longest_consec(nums):

    nums_set = set(nums)
    longest = 0

    for num in nums_set:

        if num -1 not in nums_set:
            current = num
            length = 1

            while current +1 in nums_set:
                current +=1
                length +=1

            longest = max(longest,length)

    return longest
print(longest_consec(nums))

