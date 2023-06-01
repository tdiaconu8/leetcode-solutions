from heapq import heapify, heappush, heappop

class KthLargest:

    # T: O(n), S: O(n)
    def __init__(self, k: int, nums: List[int]):
        
        self.k = k  # value of k
        self.stream = nums  # stream of numbers
        heapify(self.stream)    # Transform the stream in a heap
        while len(self.stream) > self.k:
            heappop(self.stream)

    # T: O(log(k))
    def add(self, val: int) -> int:
        heappush(self.stream, val)
        if len(self.stream) > self.k:
            heappop(self.stream)
        return self.stream[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
