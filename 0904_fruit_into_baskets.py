from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        res = 0

        counter = defaultdict(int)
        for i in range(n):
            if len(counter) < 2 or fruits[i] in counter:
                counter[fruits[i]] += 1
            else:
                lastFruit = fruits[i-1]
                res = max(res, sum(counter.values()))
                counter = defaultdict(int)
                j, c = i-1, 0
                while fruits[j] == lastFruit and j >= 0:
                    c += 1
                    j -= 1
                counter[lastFruit] = c
                counter[fruits[i]] = 1
            
        res = max(res, sum(counter.values()))
        return res

        # T: O(n^2)
        # S: O(1)
