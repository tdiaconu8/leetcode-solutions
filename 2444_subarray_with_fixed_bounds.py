class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        n = len(nums)
        res = 0
        l, prevMin, prevMax = -1, -1, -1

        for i in range(n):
            num = nums[i]
            if not (minK <= num <= maxK):
                l = i
            else:
                if num == minK:
                    prevMin = i
                if num == maxK:
                    prevMax = i
                res += max(0, min(prevMin, prevMax)-l)
            
        return res

        # T: O(n)
        # S: O(1)
