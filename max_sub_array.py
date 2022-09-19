from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        cont = [-float(inf)]*n
        cont[0] = nums[0]
        
        for i in range(1, n):
            cont[i] = max(nums[i], nums[i] + cont[i-1])
            
        return max(cont)