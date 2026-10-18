# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def porder(node):
            if node is None:
                return
            porder(node.left)      # Left
            porder(node.right)     # Right
            result.append(node.val)  # Root
        porder(root)
        return result