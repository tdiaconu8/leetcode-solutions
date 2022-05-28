from functools import lru_cache
from typing import List

# 1

def mostFrequent(self, nums: List[int], key: int) -> int:
    
    n = len(nums)
    h = {}
    
    for i in range(1,n):
        if nums[i-1] == key:
            h[nums[i]] = h.get(nums[i], 0) + 1
    return max(h, key=h.get)
# 2

def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:

    temp = []
    
    for n in nums:
        mapped = 0
        num = n
        pw = 0
        if num == 0:
            mapped = mapped + mapping[0] * 10 **(pw)
        while num > 0:
            mapped = mapped +mapping[num%10]* 10**pw
            num = num//10
            pw += 1
        temp.append((n, mapped))
    return [k for k, v in sorted(temp, key = lambda item: item[1])]

# 3

def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    
    anc = {}
    for edge in edges:
        f, t = edge
        anc[t] = anc.get(t, []) + [f]
    
    @lru_cache(None)       
    def dfs(v):
        res = []
        if v not in anc.keys():
            return tuple([v])
        else:
            res = [v]
            if v in anc.keys():
                for u in anc[v]:
                    res += list(dfs(u))
        return tuple(set(res))
    
    ans = []
    for i in range(n):
        tmp = list(dfs(i))
        tmp.remove(i)
        ans.append(sorted(tmp))
    
    return ans