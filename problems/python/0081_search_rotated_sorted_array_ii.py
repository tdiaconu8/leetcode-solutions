class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n = len(nums)

        l, r = 0, n-1

        while l <= r:
            while l <= r and l < n-1 and nums[l] == nums[l+1]:
                l += 1
            while l <=r and r > 0 and nums[r] == nums[r-1]:
                r -= 1
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l += 1
                else:
                    r -= 1
            elif nums[m] <= nums[r]:
                if nums[m] > target or nums[r] < target:
                    r -= 1
                else:
                    l += 1

        return False 