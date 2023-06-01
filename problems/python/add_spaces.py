from typing import List


def addSpaces(s: str, spaces: List[int]) -> str:
    
    shr = 0
    for i in spaces:
        s = s[0:i+shr] + ' ' + s[i+shr:]
        shr+=1
    
    return s

s="LeetcodeHelpsMeLearn"
spaces=[8,13,15]

print(addSpaces(s, spaces))