class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n = len(nums)

        # BINARY SEARCH
        l, r = 0, n-1

        while l < r:
            m = l + (r-l+1)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if nums[m] == nums[m+1]:
                m += 1
            if (m-l+1)%2 == 1:
                r = m-2
            if (m-l+1)%2 == 0:
                l = m+1
        
        return nums[l]

        # T: O(logn)
        # S: O(1)
