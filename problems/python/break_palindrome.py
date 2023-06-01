'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character 
with any lowercase English letter so that the resulting string is not a palindrome and that it is 
the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, 
return an empty string.

A string a is lexicographically smaller than a string b (of the same length) 
if in the first position where a and b differ, a has a character strictly smaller than the corresponding 
character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they 
differ is at the fourth character, and 'c' is smaller than 'd'.
'''

'''
Greedy approach
We iterate through the first half of the string
1. Replace in the first half of the string the first non 'a' char with 'a' char
2. If impossible (there are only a chars), we replace the last one with a 'b'
3. If the length of the entry is 1, we return empty as it is impossible to break the palindrome
'''

class Solution:
    def breakPalindrome(self, p: str) -> str:

        # We assume that entry is a palindrome

        n = len(p)

        for i in range(n//2):
            if p[i] != 'a':
                return p[:i] + 'a' + p[i+1:]

        return p[:n-1] + 'b' if n> 1 else ''           