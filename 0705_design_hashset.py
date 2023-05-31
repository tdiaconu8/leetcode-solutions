class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.hashSet = [ListNode(-1)] * (self.size)

    def add(self, key: int) -> None:
        index = key%self.size
        cur = self.hashSet[index]
        while cur:
            if cur.val == key:
                return
            elif not cur.next:
                cur.next = ListNode(key)
                return
            else:
                cur = cur.next

    def remove(self, key: int) -> None:
        index = key%self.size
        prev, cur = self.hashSet[index], self.hashSet[index].next
        while cur:
            if cur.val == key:
                prev.next = cur.next
                cur.next = None
                return
            prev = prev.next
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key%self.size
        cur = self.hashSet[index]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
