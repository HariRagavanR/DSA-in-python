nums = [1, 2, 3]
# nums = [7, 1, 1,10]
k = 3

def subarr_sum(nums,k):

    pre_cnt = {0:1}
    pre = 0
    cnt = 0

    for num in nums:
        pre += num
        needed = pre - k

        if needed in pre_cnt:
            cnt += pre_cnt[needed]

        pre_cnt[pre] = pre_cnt.get(pre,0) + 1

    return cnt

print(subarr_sum(nums,k))

""" 
Leet code soln:


def subarraySum(self, nums: List[int], k: int) -> int:
    res = curSum = 0
    prefixSums = { 0 : 1 }

    for num in nums:
        curSum += num
        diff = curSum - k

        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

    return res

"""