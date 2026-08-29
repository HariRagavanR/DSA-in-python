nums = [1, 3, 3, 3, 3, 8]
target = 3

def first_occurance(nums):
    left = 0
    right = len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left + right) //2

        if nums[mid] == target:
            ans = mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid -1

    return ans

print(first_occurance(nums))

