class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        # NEW ARRAY CREATION
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        
        return res

        # T: O(n)
        # S: O(2n)

        # NO EXTRA SPACE METHOD
        # we store x, y values in the first half using bits calculation
        '''
        for i in range(n):
            nums[i] = nums[i]<<10
            nums[i] = nums[i] | nums[i+n]
        
        for i in range(n-1, -1, -1):
            j = n-1-i
            y = nums[i] & (2**10-1)
            x = nums[i]>>10
            nums[2*n-1-2*j] = y
            nums[2*n-1-2*j-1] = x
        
        return nums

        # T: O(2*n)
        # S: O(1)
        '''
