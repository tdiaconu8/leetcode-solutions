from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # T: O(n)
        # S: O (1)

        res = ListNode(0, head)
        prev, cur = res, head

        while cur and cur.next:
            
            nextPair = cur.next.next # next node starting of the next pair (two next operations)

            prev.next = cur.next
            cur.next.next = cur
            cur.next = nextPair

            prev, cur = prev.next.next, cur.next
            
        return res.next
