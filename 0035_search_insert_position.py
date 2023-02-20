class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)

        # BINARY SEARCH
        l, r = 0, n-1
        while l < r:
            middle = (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle-1
            elif nums[middle] < target:
                l = middle + 1
        
        return l+1 if nums[l] < target else l

        # T: O(logn)
        # S: O(1)
