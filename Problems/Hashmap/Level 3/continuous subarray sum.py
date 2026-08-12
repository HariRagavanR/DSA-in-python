nums = [23, 2, 4, 6, 7]
k = 6

def check_subarray_sum(nums, k):

    remainder_index = {0: -1}

    prefix = 0

    for i, num in enumerate(nums):

        prefix += num

        remainder = prefix % k

        if remainder in remainder_index:

            if i - remainder_index[remainder] >= 2:
                return True

        else:
            remainder_index[remainder] = i

    return 

print(check_subarray_sum(nums,k))

