'''
Given a string s, reverse the order of characters in each word within 
a sentence while still preserving whitespace and initial word order.
'''

class Solution:
    def reverseWords(self, s: str) -> str:

        words = [word for word in s.split()]
        res = []
        
        for w in words:
            res.append(w[::-1])
        
        return ' '.join(word for word in res)