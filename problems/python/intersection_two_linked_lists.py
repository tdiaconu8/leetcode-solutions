# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        n, m, p1, p2 = 0, 0, headA, headB
        while p1:
            n += 1
            p1 = p1.next
        while p2:
            m += 1
            p2 = p2.next 
        p1, p2 = headA, headB
        while n > m:
            p1 = p1.next
            n -= 1 
        while m > n:
            p2 = p2.next
            m -= 1 
        while p1:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next 
        return None
        
        '''
        T: O(n+m)
        S: O(1)
        '''
        
        '''
        p1, p2 = headA, headB
        reached = set()
        
        while p1:
            reached.add(p1)
            p1 = p1.next
            
        while p2:
            if p2 in reached:
                return p2
            p2 = p2.next
            
        return None
        '''
        '''
        T: O(n+m)
        S: O(n)
        '''