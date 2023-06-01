# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ans = ListNode(0)
        res = ans
        
        nodes = []
        
        while head:
            nodes.append(head.val)
            head = head.next
        
        n = len(nodes)
        nodes[k-1], nodes[n-k] = nodes[n-k], nodes[k-1]
        
        for i in range(n):
            res.next = ListNode()
            res = res.next
            res.val = nodes[i]
            
        return ans.next
    
    '''
    Time : O(n)
    Space : O(n)
    '''