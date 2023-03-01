class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # DIVIDE AND CONQUER

        def merge(left, right):
            res = []
            p1, p2 = 0, 0

            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2]:
                    res.append(left[p1])
                    p1 += 1
                else:
                    res.append(right[p2])
                    p2 += 1
            
            while p1 < len(left):
                res.append(left[p1])
                p1 += 1
            
            while p2 < len(right):
                res.append(right[p2])
                p2 += 1
            
            return res


        n = len(nums)
        if n == 1:
            return [nums[0]]
        
        return merge(self.sortArray(nums[:n//2]), self.sortArray(nums[n//2:]))

        # T: O(nlogn)
        # S: O(1) -> no extra space
