nums = [-4, -1, 0, 3, 10]

def sorted_sqrs(nums):

    n = len(nums)
    result = [0]*n

    left = 0
    right = n -1
    
    for position in range(n-1,-1,-1):

        if abs(nums[left]) > abs(nums[right]):
            result[position] = nums[left] **2
            left +=1

        else:
            result[position] = nums[right] **2
            right -=1

    return result 

print(sorted_sqrs(nums))

"""
leetcode solution:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num*num)
        result.sort()
        return result

"""