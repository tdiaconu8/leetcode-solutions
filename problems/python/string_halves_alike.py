class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        counterA, counterB = 0, 0
        
        for i in range(n//2):
            if s[i] in vowels:
                counterA += 1
            if s[-i-1] in vowels:
                counterB += 1
        
        return counterA == counterB

'''
T: O(n/2)
S: O(1)
'''