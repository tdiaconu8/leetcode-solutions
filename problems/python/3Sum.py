from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    
    if len(nums) < 3:
        return []
    
    counter, ans, n = {}, [], len(nums)
    for i in range(len(nums)):
        counter[nums[i]] = counter.get(nums[i], 0) + 1
    
    dist = sorted(list(counter.keys()))
    
    for i, cur in enumerate(dist):
        target = -cur
        l, r = 0, len(dist)-1
        while l <= r:
            if dist[l] + dist[r] < target:
                l += 1
            elif dist[l] + dist[r] > target:
                r -= 1
            else:
                if i < l < r:
                    ans.append([cur, dist[l], dist[r]])
                elif i==l <r and counter[cur] >=2:
                    ans.append([cur, cur, dist[r]])
                elif i<l==r and counter[dist[l]] >=2:
                    ans.append([cur, dist[l], dist[r]])
                elif i == l == r and counter[cur] >= 3:
                    ans.append([cur, cur, cur])
                l += 1
                r -= 1
                
    return ans

'''
Time : O(n**2)
Space : O(n)
'''