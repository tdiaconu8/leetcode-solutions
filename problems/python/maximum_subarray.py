from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    
    n = len(nums)
    sums = [0] * n
    sums[0] = nums[0]
    
    for i in range(1,n):
        sums[i] = max(nums[i], nums[i]+sums[i-1])
        
    return max(sums)
    
    '''
    Time : O(n)
    Space : O(n)
    '''