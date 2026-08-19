nums = [1, 12, -5, -6, 50, 3]
k = 4

def max_avg(nums,k):
    left = 0
    window_sum = 0
    max_sum = float('-inf')

    for right in range(len(nums)):

        window_sum += nums[right]

        if right - left +1 == k:
            max_sum = max(max_sum,window_sum)
            window_sum -= nums[left]
            left +=1

    return max_sum / k

print(max_avg(nums,k))
