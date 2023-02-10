class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = {0: set([i for i in range(size)]), 1: set()} # S: O(n)

    def fix(self, idx: int) -> None:  # O(1)
        if idx in self.bits[0]:
            self.bits[0].remove(idx)
            self.bits[1].add(idx)

    def unfix(self, idx: int) -> None: # O(1)
        if idx in self.bits[1]:
            self.bits[1].remove(idx)
            self.bits[0].add(idx)

    def flip(self) -> None: # O(1)
        self.bits[0], self.bits[1] = self.bits[1], self.bits[0]

    def all(self) -> bool: # O(1)
        return len(self.bits[1]) == self.size

    def one(self) -> bool: # O(1)
        return len(self.bits[1]) > 0

    def count(self) -> int: # 0(1)
        return len(self.bits[1])

    def toString(self) -> str: # O(2.n), extra space O(n)
        res = [0] * self.size
        for idx in self.bits[1]:
            res[idx] = 1
        return ''.join(str(bit) for bit in res)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
