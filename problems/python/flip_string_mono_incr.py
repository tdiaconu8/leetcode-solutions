class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        n = len(s)
        leftFlips, rightFlips = 0, s.count('0')
        res = rightFlips

        for i in range(n):
            char = s[i]
            if char == '1':
                leftFlips += 1
            elif char == '0':
                rightFlips -= 1
            res = min(res, rightFlips + leftFlips)
        
        return res

        '''
        T: O(n)
        S: O(1)
        '''
