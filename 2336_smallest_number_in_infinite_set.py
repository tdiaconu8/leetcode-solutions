from heapq import heapify, heappop, heappush

class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1001)]
        self.setValues = set([i for i in range(1, 1001)])
        heapify(self.nums)

    def popSmallest(self) -> int:
        res = heappop(self.nums)
        self.setValues.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if num not in self.setValues:
            heappush(self.nums, num)
            self.setValues.add(num)
    
    # T: O(nlogn)
    # S: O(n)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
