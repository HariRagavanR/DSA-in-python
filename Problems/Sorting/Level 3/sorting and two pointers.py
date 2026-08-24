def find_pair(nums, target):

    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:

        total = nums[left] + nums[right]

        if total == target:
            return [nums[left], nums[right]]

        elif total < target:
            left += 1

        else:
            right -= 1

    return []

nums = [8, 3, 2, 7, 5]

print(find_pair(nums, 10))