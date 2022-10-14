from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        tmp = head
        lookup = {}
        i = 0

        while tmp:
            lookup[i] = tmp
            tmp = tmp.next
            i += 1
        
        middle = i//2
        lookup[middle-1].next = lookup[middle].next

        return head