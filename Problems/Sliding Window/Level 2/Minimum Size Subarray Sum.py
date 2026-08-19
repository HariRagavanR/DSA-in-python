target = 7
nums = [2,3,1,2,4,3]

def min_subarr_len(target, nums):

    left = 0
    wind_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):

        wind_sum += nums[right]

        while wind_sum >= target:
            curr_len = right - left +1
            min_len = min(min_len, curr_len)
            wind_sum -= nums[left]
            left +=1

    if min_len == float('inf'):
        return 0

    return min_len

print(min_subarr_len(target,nums))



