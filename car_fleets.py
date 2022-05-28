from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    
    n, data = len(speed), []
    for i in range(n):
        data.append((position[i], speed[i]))
    
    data.sort(key=lambda x: x[0])
    
    fleets = []
    
    for i in range(n-1, -1, -1):
        fleets.append(data[i])
        if len(fleets) >= 2:
            t1, t2 = (target - fleets[-1][0])/fleets[-1][1], (target - fleets[-2][0])/fleets[-2][1]
            if t1 <= t2:
                fleets.pop()
    
    return len(fleets)

'''
Time : O(n)
Space : O(n)
'''