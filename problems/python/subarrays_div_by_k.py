class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        res = 0
        rems = {0: 1}
        curSum = 0

        for num in nums:
            curSum += num
            rem = curSum %k
            diff = rem
            res += rems.get(diff, 0)
            rems[rem] = 1 + rems.get(rem, 0)
        
        return res
