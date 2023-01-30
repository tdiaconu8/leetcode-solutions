from collections import defaultdict

class ListNode:

    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:

    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}  # map the key to the node
    
    def length(self):
        return len(self.map)
    
    def insert(self, key, val):  # insert a new value in the node
        node = ListNode(key, val, self.right.prev, self.right)
        self.map[key] = node
        node.prev.next, self.right.prev = node, node
    
    def remove(self, key):
        if key in self.map:
            node = self.map[key]
            left, right = node.prev, node.next
            left.next, right.prev = right, left
            del self.map[key]
    
    def removeLru(self):
        res = self.left.next.key
        self.remove(res)
        return res

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity # capacity of the cache
        self.cache = {} # map the key to the value
        self.counter = {} # map the key to the frequence
        self.groups = defaultdict(LinkedList) # map the freq group to the corresponding linked list
        self.minFreq = 0  # min freq for lfu eviction

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            val, freq = self.cache[key], self.counter[key]
            self.groups[freq].remove(key)
            self.groups[freq+1].insert(key, val)
            self.counter[key] = freq+1
            if freq == self.minFreq and self.groups[freq].length() == 0:
                self.minFreq = freq+1
            return val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.cache and len(self.cache) == self.cap:  # only case of eviction
            lfuList = self.groups[self.minFreq]
            lfuKey = lfuList.removeLru()
            del self.cache[lfuKey]
            del self.counter[lfuKey]
        self.cache[key] = value
        freq = self.counter.get(key, 0)
        self.groups[freq].remove(key)
        self.groups[freq+1].insert(key, value)
        self.counter[key] = freq+1
        if freq == self.minFreq and self.groups[freq].length() == 0:
                self.minFreq = freq+1
        self.minFreq = min(self.minFreq, self.counter[key])
