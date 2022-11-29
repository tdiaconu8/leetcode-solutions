import random
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.vals = [] # array with the values
        self.idx = {}  # Map value to index

    def insert(self, val: int) -> bool:
        # O(1)
        if val in self.idx and self.idx[val] != -1:
            return False 
        self.vals.append(val)
        self.idx[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        # O(1)
        if val not in self.idx or self.idx[val] == -1:
            return False
        i = self.idx[val]
        self.idx[self.vals[-1]] = i
        self.vals[-1], self.vals[i] = self.vals[i], self.vals[-1] 
        self.vals.pop()
        self.idx[val] = -1
        return True

    def getRandom(self) -> int:
        # O(1)
        n = len(self.vals)
        print(n)
        rd = random.randint(0, n-1)
        return self.vals[rd]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()