nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarr(nums, k):

    left = 0 
    window_sum = 0
    max_sum = float('-inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left +1 == k:

            max_sum = max(max_sum, window_sum)

            window_sum -= nums[left]

            left += 1

    return max_sum

print(max_sum_subarr(nums,k))

