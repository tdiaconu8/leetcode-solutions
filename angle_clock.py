def angleClock(hour: int, minutes: int) -> float:
    
    hour_Hand, min_Hand = 0, 0
    
    min_Hand = minutes
    hour_Hand = (hour*5)%60 + minutes/60 * 5
    
    angle = max(min_Hand, hour_Hand) - min(min_Hand, hour_Hand)
    
    return min(angle*6, 360 - angle*6)

'''
Time : O(1)
Space : O(1)
'''