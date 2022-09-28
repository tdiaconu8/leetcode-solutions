# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    T : O(n)
    S : O(n²)/O(n)
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Edge case
        if not head or not head.next:
            return None
        
        iterator, nodes = head, {}
        i = 0
        
        while iterator:
            nodes[i] = iterator
            i += 1
            iterator = iterator.next
        L = i
        
        if n == L:
            return head.next
        
        nodes[L-n-1].next = nodes[L-n-1].next.next
        return head