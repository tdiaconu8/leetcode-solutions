class Solution:
    def frequencySort(self, s: str) -> str:

        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        groups, freq = {}, []

        for k, v in counter.items():
            groups[v] = groups.get(v, []) + [k]
            if v not in freq:
                freq.append(v)

        freq = sorted(freq)[::-1]

        res = ''
        for f in freq:
            for char in groups[f]:
                res += char*f
        return res