class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # T: O(log(n))
        # S: O(1)

        n = len(nums)

        l, r = 0, n-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # left part of the array is sorted
                if nums[m] < target or nums[l] > target:
                    l = m+1
                else:
                    r = m-1
            elif nums[m] <= nums[r]:    # right part is sorted
                if nums[m] > target or nums[r] < target:
                    r = m-1
                else:
                    l = m+1
        
        return -1
        