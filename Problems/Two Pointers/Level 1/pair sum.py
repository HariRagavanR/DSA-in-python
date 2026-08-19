nums = [1, 2, 3, 4, 6]
target = 6

def pair_sum(nums,target):

    left = 0
    right = len(nums) -1

    while left < right:

        total = nums[left] + nums[right]

        if total == target:
            return True

        elif total < target:
            left +=1

        else:
            right -=1

    return False

print(pair_sum(nums, target))

