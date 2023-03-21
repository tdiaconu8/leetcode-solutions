class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        zeroes = 0
        res = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeroes += 1
            else:
                res += zeroes*(zeroes+1)/2
                zeroes = 0

        return int(res + zeroes*(zeroes+1)/2)

        # T: O(n)
        # S: O(1)
