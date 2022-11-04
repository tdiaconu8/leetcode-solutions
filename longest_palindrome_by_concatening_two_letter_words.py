from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        res = 0
        lookup = {}

        for w in words:
            if w in lookup and lookup[w] > 0:
                res += 4
                lookup[w] -= 1
            else:
                lookup[w[::-1]] = lookup.get(w[::-1], 0) + 1
        
        for w in lookup:
            if lookup[w] > 0 and w[0] == w[1]:
                res += 2
                break

        return res