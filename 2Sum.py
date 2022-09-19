from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        for i, num in enumerate(nums):
            rem = target-num
            if rem in lookup:
                return [i, lookup[rem]]
            lookup[num] = i
        
        return