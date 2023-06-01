from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    
    people.sort()
    p1, p2 = 0, len(people)-1
    ans = 0
    
    while p1 < p2:
        if people[p1] + people[p2] <= limit:
            ans += 1
            p2 -= 1
            p1 += 1
        else:
            ans += 1
            p2 -= 1
    
    if p1 == p2:
        ans += 1
        
    return ans

# Time : O(nlog(n))
# Space : O(1)