from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # T: O(klogn)
        # S: O(1)

        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        heapify(nums)

        while k > 1:
            heappop(nums)
            k -= 1
        
        return -heappop(nums)