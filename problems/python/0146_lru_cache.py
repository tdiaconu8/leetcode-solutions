class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # map key to the list node
        self.mxCap = capacity  # max capacity
        self.cap = 0  # current capacity of the cache
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
            self.cap -= 1
        if self.cap == self.mxCap:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
            self.cap -= 1
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node
        self.cap += 1
    
    def insert(self, node): # insert a node in the linked list
        tmp = self.right.prev
        self.right.prev, node.next = node, self.right
        node.prev, tmp.next = tmp, node
    
    def remove(self, node): # remove node from the linked list
        left, right = node.prev, node.next
        left.next, right.prev = right, left
