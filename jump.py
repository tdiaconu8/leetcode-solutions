from typing import List


def jump(nums: List[int]) -> int:
    
    n = len(nums)
    if n ==1: return 0
    
    dp = [n+1] * n
    dp[0] = 0
    
    for i in range(n-1):
        j = nums[i]
        for k in range(i+1, min(n,i+1+j)):
            dp[k] = min(dp[k], dp[i] + 1)
    
    print(dp)
    return dp[-1]

'''
Time : O(n²)
Space : O(n)
'''