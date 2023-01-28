class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        # insert value in arr
        self.arr.append(value)
        i = len(self.arr)-1
        while i > 0 and self.arr[i-1] > self.arr[i]:
            self.arr[i], self.arr[i-1] = self.arr[i-1], self.arr[i]
            i -= 1

    def getIntervals(self) -> List[List[int]]:
        if not self.arr: return []
        res = [[self.arr[0], self.arr[0]]]
        s, e = res[-1]
        for i in range(1, len(self.arr)):
            num = self.arr[i]
            if s <= num <= e:
                continue
            if num == e + 1:
                res[-1][1] = num
            else:
                res.append([num, num])
            s, e = res[-1]
        return res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
