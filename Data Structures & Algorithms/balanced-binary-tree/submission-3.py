# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(root):
            if not root:
                return [0,True]
            left=recurse(root.left)
            right=recurse(root.right)
            balanced= left[1] and right[1] and abs(left[0]-right[0])<2
            height=1 + max(left[0],right[0])
            return [height,balanced]
        return recurse(root)[1]