class Solution:
    def addDigits(self, num: int) -> int:

        while num//10:
            tmp = 0
            while num:
                tmp += num%10
                num = num//10
            num = tmp
        
        return num

        # T: O(n) where n is the nb of digits
        # S: O(1)
