# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def sameTree(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1 and r2 and r1.val==r2.val:
                return sameTree(r1.left,r2.left) and sameTree(r1.right,r2.right)
            return False
        
        def bfs(root,sub):
            if not sub:
                return True
            if not root:
                return False
            if sameTree(root,sub):
                return True
            return bfs(root.left,sub) or bfs(root.right,sub)
        return bfs(root,subRoot)