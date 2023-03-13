from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        heapify(heap)

        for i in range(len(lists)):
            linkedList = lists[i]
            if linkedList:
                heappush(heap, (linkedList.val, i, linkedList))
        
        res = ListNode()
        cur = res
        while heap:
            val, id, linkedList = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            linkedList = linkedList.next
            if linkedList:
                heappush(heap, (linkedList.val, id, linkedList))
        
        return res.next
      
      # T: O(n.logk)
      # S: O(n)
