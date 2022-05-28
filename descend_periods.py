from typing import List


def getDescentPeriods(prices: List[int]) -> int:
    
    n = len(prices)
    ans = n
    
    ind = 0
    cur = 0
    
    while ind <n-1:    
        if prices[ind] - prices[ind+1] == 1:
            cur += 1
        else:
            ans += sum(i for i in range(cur+1))
            cur = 0
        ind +=1
    if cur >0:
        return ans + sum(i for i in range(cur+1))

prices=[12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7]
print(getDescentPeriods(prices))