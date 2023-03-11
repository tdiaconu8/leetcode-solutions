# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        def buildBST(values):
            if not values:
                return
            res = TreeNode()
            m = len(values)//2
            res.val = values[m]
            res.left = buildBST(values[:m])
            res.right = buildBST(values[m+1:])
            return res
        
        return buildBST(values)

        # T: O(n)
        # S: O(n)
