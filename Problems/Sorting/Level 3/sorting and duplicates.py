def contains_duplicate(nums):

    nums.sort()

    for i in range(1, len(nums)):

        if nums[i] == nums[i - 1]:
            return True

    return False

nums = [5, 3, 8, 3, 1]

print(contains_duplicate(nums))