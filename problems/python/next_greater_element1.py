from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    
    
    n, m = len(nums1), len(nums2)
    ans, pos = [-1 for _ in range(n)], {v:i for i,v in enumerate(nums1)}
    stack = []
    
    for i in range(m):
        while stack and stack[-1] < nums2[i]:
            pop = stack.pop()
            if pop in pos.keys():
                idx = pos[pop]
                ans[idx] = nums2[i]
        stack.append(nums2[i])
    
    return ans
    
    '''
    Time: O(n+m)
    Space: O(n+m)
    '''


    n, m = len(nums1), len(nums2)
    ans = [0] * n
    pos = {}
    
    for i, val  in enumerate(nums2):
        pos[val] = i + pos.get(val, 0)
    
    def nextGreat(l, val):
        for i in range(len(l)):
            if l[i] > val:
                return l[i]
        return -1
    
    for j in range(n):
        if pos[nums1[j]] == m-1:
            ans[j] = -1
        else:
            ans[j] = nextGreat(nums2[pos[nums1[j]]:], nums1[j])
    
    return ans

    '''
    Time : O(n*m)
    Space : O(m+n)
    '''