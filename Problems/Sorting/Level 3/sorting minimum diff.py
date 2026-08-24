def minimum_difference(nums):

    nums.sort()

    min_diff = float('inf')

    for i in range(1, len(nums)):

        diff = nums[i] - nums[i - 1]

        min_diff = min(min_diff, diff)

    return min_diff

nums = [10, 3, 6, 20, 8]

print(minimum_difference(nums))