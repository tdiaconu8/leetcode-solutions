from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    
    n = len(nums)
    res, stack = [-1 for _ in range(n)], []
    
    for _ in range(2):
        for i, val in enumerate(nums):
            while stack and stack[-1][0] < val:
                ind = stack.pop()[1]
                res[ind] = val
            stack.append((val,i))
    
    return res

    '''
    Time: O(n)
    Space: O(n)

    [1, 2, 3, 4, 3]
    [2, 3, 4,-1,-1]               [(4,3), (3,4), (3,2)]
    '''
    
    
    
    
    
    # O(n*n), O(n)
    '''
    n = len(nums)
    if n == 1: return [-1]
    ans = [-1] * n
    def greater(L, val):
        for num in L:
            if num > val: return num
        return -1
    for i, n in enumerate(nums):
        ans[i] = greater(nums[i+1:] + nums[:i], n)
    return ans
    '''