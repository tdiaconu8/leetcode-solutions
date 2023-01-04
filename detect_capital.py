class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        n = len(word)
        caps = 0

        for i in range(n):
            char = word[i]
            if char.lower() != char:
                caps += 1
        
        if caps == 0:
            return True
        if caps == 1:
            return word[0].lower() != word[0]
        else:
            return caps == n
        
        '''
        T: O(n)
        S: O(1)
        '''