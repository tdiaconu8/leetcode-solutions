class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        lookup = {char: i for i, char in enumerate(order)}

        def isLower(w1, w2): # helper function which return true if w1 <= w2, else false
            i = 0
            while i < min(len(w1), len(w2)):
                if lookup[w1[i]] < lookup[w2[i]]:
                    return True
                elif lookup[w1[i]] > lookup[w2[i]]:
                    return False
                i += 1
            return len(w1) <= len(w2)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1] # we compare each pair
            if not isLower(w1, w2):
                return False
        return True

        '''
        len(words) = n, max(len(word)) = m, len(order) = p
        T: O(p+n*m)
        S: O(p)
        '''
