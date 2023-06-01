# 1

from cmath import inf
from typing import List


def minimumSum(num: int) -> int:
    
    numbers = []
    while num > 0:
        numbers.append(num%10)
        num = num //10
    numbers.sort()
    a, b = 0, 0
    for i in range(len(numbers)):
        if i%2 != 0:
            a = 10*a + numbers[i]
        else:
            b = 10*b + numbers[i]
    return a+b

#print(minimumSum(4009))

# 2

def pivotArray(nums: List[int], pivot: int) -> List[int]:
    
    leftArr = []
    rightArr = []
    nbPivot = 0
    
    for i in range(len(nums)):
        if nums[i] < pivot:
            leftArr.append(nums[i])
        elif nums[i] > pivot:
            rightArr.append(nums[i])
        elif nums[i] == pivot:
            nbPivot += 1
    return leftArr + [pivot]*nbPivot + rightArr

#print(pivotArray([-3,4,3,2], 2))

# 3
def minCostSetTime(startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

    cost = inf

    # Find possible ways  
    ways = []
    mns = targetSeconds//60
    sec = targetSeconds%60
    if 1 <= mns <= 99:
        ways.append(mns * 100 + sec)
        if sec <= 39:
            ways.append((mns-1)*100+sec+60)
    if mns == 100:
        ways.append((mns-1)*100+sec+60)
    if mns < 1:
        ways.append(sec)
    print(ways)
    for w in ways:
        digits = list(map(int, str(w)))
        curr = startAt
        curr_cost = 0
        for i in range(len(digits)):
            if curr == digits[i]:
                curr_cost += pushCost
            else:
                curr_cost += moveCost
                curr_cost += pushCost
                curr = digits[i]
        cost = min(cost, curr_cost)
    return cost

    # Find the minimum cost for each way
# print(minCostSetTime(9,100000,1,targetSeconds=6039))
print(minCostSetTime(1,9403,9402,targetSeconds=6008))