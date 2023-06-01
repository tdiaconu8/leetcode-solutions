class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        n = len(s)
        ans = 0
        counter = {}

        for i in range(0, n - minSize+1):
            sub, unq = '', 0
            for j in range(i, min(i + maxSize, n)):
                if unq > maxLetters:
                    break
                else:
                    if sub.count(s[j]) == 0:
                        unq += 1
                    if unq > maxLetters:
                        break
                    sub += s[j]
                    if len(sub) >= minSize:
                        counter[sub] = counter.get(sub, 0) + 1
                        ans = max(ans, counter[sub])
        
        return ans
    
    # T : O(n * 26)
    # S : O(n)