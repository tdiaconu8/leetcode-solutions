from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        pos = n-1 # initialize a pos variable to store the minimum starting point to reach the end

        for i in range(n-1, -1, -1):
            if nums[i] + i >= pos:  # if jump goes over pos, the current position becomes pos
                pos = i
        
        return pos == 0 # if pos is 0, true, else false
    
    '''
    T: O(n)
    S: O(1)
    '''