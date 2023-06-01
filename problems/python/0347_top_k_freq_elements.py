from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Bucket sort
        # T: O(n), S: O(n)
        n = len(nums)
        counter = Counter(nums)
        freq = [[] for _ in range(n+1)]
        for num, c in counter.items():
            freq[c].append(num)
        res = []
        for i in range(n, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # HEAP approach
        # T: O(k*log(n))
        # S: O(n)
        '''
        counter = Counter(nums)
        heap = []
        for n, c in counter.items():
            heappush(heap, (-c, n))

        res = []
        while k > 0:
            res.append(heappop(heap)[1])
            k -= 1

        return res
        '''
