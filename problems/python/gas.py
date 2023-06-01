from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    
    n = len(gas)

    # Coin edge
    if sum(gas) < sum(cost):
        return -1

    else:
        # list of what the tank contains starting from 0 for each station
        tank = [gas[0]] * n
        for i in range(1,n):
            tank[i] = tank[i-1] + gas[i-1] - cost[i-1]
        return tank.index(min(tank))

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

# gas = [2,3,4]
# cost = [3,4,3]

print(canCompleteCircuit(gas, cost))
