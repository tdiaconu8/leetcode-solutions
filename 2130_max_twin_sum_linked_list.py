# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # NO EXTRA SPACE
        # T: O(n), S: O(1)
        
        res = 0
        
        # Find the second part of the array (containing twin nodes)
        twin, fast = head, head
        while fast and fast.next:
            twin = twin.next
            fast = fast.next.next
        
        # Reverse the twin linked list
        prev = None
        while twin:
            nxt = twin.next
            twin.next = prev
            prev = twin
            twin = nxt

        # Compute max sum
        while prev:
            res = max(res, prev.val + head.val)
            head, prev = head.next, prev.next
        return res


        # EXTRA SPACE: using array to store values
        # T: O(n), S: O(n)
        '''
        node = head
        vals = []

        while node:
            vals.append(node.val)
            node = node.next
        
        res, i = 0, 0

        while i < len(vals)/2:
            res = max(res, vals[i]+vals[-i-1])
            i += 1
        
        return res
        '''
