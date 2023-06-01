from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        tmp = head

        while tmp:
            i += 1
            tmp = tmp.next
        
        n, i = i, 0
        middle = n//2

        while i < middle:
            head = head.next
            i += 1
        
        return head