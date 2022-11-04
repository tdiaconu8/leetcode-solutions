class Solution:
    def reverseVowels(self, s: str) -> str:

        vowelsWord = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for char in s:
            if char.lower() in vowels:
                vowelsWord.append(char)
        
        vowelsWord = vowelsWord[::-1]

        res = []
        i = 0

        for char in s:
            if char.lower() in vowels:
                res.append(vowelsWord[i])
                i += 1
            else:
                res.append(char)
        
        return ''.join(char for char in res)