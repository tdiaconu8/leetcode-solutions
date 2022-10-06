'''
Design a time-based key-value data structure that can store multiple values 
for the same key at different time stamps and retrieve the key's value at a certain timestamp.
'''

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        vals = self.map[key]
        l, r = 0, len(vals)-1
        while l <= r:
            m = (l+r)//2
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m+1
            else:
                r = m-1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)