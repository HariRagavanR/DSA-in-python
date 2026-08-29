nums = [8, 3, 7, 1, 5]

target = 7

def linear_search(nums):

    for i in range(len(nums)):

        if nums[i] == target:
            return i

    return -1

print(linear_search(nums))

