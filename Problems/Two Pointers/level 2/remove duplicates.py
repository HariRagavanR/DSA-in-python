nums = [1,1,2,2,3]

def remove_dup(nums):

    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:
            slow +=1

            nums[slow] = nums[fast]

    return slow + 1

print(remove_dup(nums))

