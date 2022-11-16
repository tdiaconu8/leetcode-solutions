# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l, r = 0, n+1
        middle = (l+r)//2

        while guess(middle) != 0:
            if guess(middle) == -1:
                r = middle
            elif guess(middle) == 1:
                l = middle
            middle = (l+r)//2
        
        return middle