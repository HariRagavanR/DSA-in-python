nums = [2,7,11,15]
target = 9

def two_sum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        total = nums[left] + nums[right]

        if total == target:
            return [left, right]

        elif total < target:
            left += 1

        else:
            right -= 1

    return []

print(two_sum(nums,target))