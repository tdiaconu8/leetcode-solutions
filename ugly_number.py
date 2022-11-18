class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        
        # Idea : is a number is ugly, it has only 2,3 and 5 as prime dividers, thus it can be written as n = 2**p * 3**q * 5**r

        for i in [2, 3, 5]:
            while n%i == 0:
                n /= i
        return n == 1