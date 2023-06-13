class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # T: O(n)
        # S: O(n)

        n = len(nums)
        res = []

        if not nums: 
            return res

        start, prev = nums[0], nums[0]

        for i in range(1, n):
            if nums[i] == prev + 1:
                prev = nums[i]
                continue
            if start == prev:
                res.append(str(start))
            elif start != prev:
                res.append(str(start)+"->"+str(prev))
            start, prev = nums[i], nums[i]
        
        if start == prev:
            res.append(str(start))
        elif start != prev:
            res.append(str(start)+"->"+str(prev))
        return res