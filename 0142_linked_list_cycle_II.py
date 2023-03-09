# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # TORTOISE AND HARE ALGORITHM

        if not head or not head.next:
            return None

        tortoise, hare = head.next, head.next.next

        while hare and hare.next:
            if tortoise == hare:
                tortoise = head
                while tortoise != hare:
                    tortoise, hare = tortoise.next, hare.next
                return tortoise
            tortoise = tortoise.next
            hare = hare.next.next
        
        return None

        # T: O(n)
        # S: O(1)
