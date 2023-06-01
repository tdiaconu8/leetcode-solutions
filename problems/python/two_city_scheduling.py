from typing import List


def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    
    diff = []
    for c1, c2 in costs:
        diff.append([c2 - c1, c1, c2])
    diff.sort()
    ans = 0
    for i in range(len(diff)):
        if i<len(diff)//2:
            ans += diff[i][2]
        else:
            ans += diff[i][1]
    return ans

# Time : O(nlogn)
# Space : O(n)