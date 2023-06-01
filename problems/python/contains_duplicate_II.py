from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        ind = {}

        for i, num in enumerate(nums):
            if (num in ind) and (i - ind[num] <= k):
                    return True
            ind[num] = i

        return False       