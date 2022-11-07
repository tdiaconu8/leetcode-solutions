class Solution:
    def maximum69Number (self, num: int) -> int:

        n = num

        nums = []
        while n > 0:
            n, r = n//10, n%10
            nums.append(r)
        
        nums = nums[::-1]
        changed = False

        for i in range(len(nums)):
            if changed:
                break
            else:
                if nums[i] == 6:
                    nums[i] = 9
                    changed = True
        res = 0
        for i in range(len(nums)):
            res = 10*res + nums[i]
        
        return res