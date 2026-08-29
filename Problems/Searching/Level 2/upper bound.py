nums = [1, 2, 2, 2, 4, 5]
target = 2

def upper_bound(nums):
    left = 0
    right = len(nums) -1
    ans = len(nums)

    while left <= right:
        mid = (left+right) //2
        if nums[mid] > target:
            ans = mid
            right = mid -1

        else:
            left = mid + 1

    return ans

print(upper_bound(nums))
