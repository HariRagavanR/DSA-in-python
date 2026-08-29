nums = [1,3,3,5,7]
target = 4

def lower_bound(nums):
    left = 0
    right = len(nums) -1
    ans = len(nums)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            ans = mid
            right = mid -1

        else:
            left = mid +1

    return ans

print(lower_bound(nums))
