nums = [1, 2, 1, 0, 1, 1, 0]
k = 4

def long_subarr(nums, k):
    left = 0
    max_len = 0
    wind_sum = 0

    for right in range(len(nums)):

        wind_sum += nums[right]

        while wind_sum > k:
            wind_sum -= nums[left]
            left += 1

        cur_len = right - left + 1

        max_len = max(max_len, cur_len)

    return max_len

print(long_subarr(nums,k))
        