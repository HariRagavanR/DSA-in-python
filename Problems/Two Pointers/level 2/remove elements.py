nums = [3,2,2,3]
target = 3

def remove_element(nums, target):

    slow = 0

    for fast in range(len(nums)):

        if nums[fast] != target:
            nums[slow] = nums[fast]
            slow += 1

    return slow

print(remove_element(nums,target))


