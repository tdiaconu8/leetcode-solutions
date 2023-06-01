class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        wordToPattern = {}
        patternToWord = {}

        words = s.split()

        if len(pattern) != len(words):
            return False
        
        for i, word in enumerate(words):
            curPattern = pattern[i]
            if word not in wordToPattern:
                if curPattern in patternToWord:
                    return False
                else:
                    wordToPattern[word] = curPattern
                    patternToWord[curPattern] = word
            else:
                if wordToPattern[word] != curPattern:
                    return False
        
        return True

        '''
        T: O(n)
        S: O(n)
        '''