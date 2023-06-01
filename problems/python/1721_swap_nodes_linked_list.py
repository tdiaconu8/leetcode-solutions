from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # TWO POINTER: no extra space
        # T: O(n)
        # S: 0(1)
        
        node = head
        for i in range(k-1):
            node = node.next
        l, r = node, head

        while node.next:
            r = r.next
            node = node.next
        
        l.val, r.val = r.val, l.val

        return head
        
        
        
        # HASHMAP EXTRA SPACE
        # T: O(n)
        # S: O(n)
        
        nodes = defaultdict(int)
        i = 0

        node = head
        while node:
            nodes[i] = node
            node = node.next
            i += 1
        n = i

        l, r = k-1, n-k
        nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val 

        return head
