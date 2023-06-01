from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        idx = len(nums)-1
        
        while idx >= 0:
            if nums[idx] == val:
                k += 1
                j = idx
                while j < len(nums)-1 and nums[j+1] != val:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
            idx -= 1
        
        return len(nums)-k