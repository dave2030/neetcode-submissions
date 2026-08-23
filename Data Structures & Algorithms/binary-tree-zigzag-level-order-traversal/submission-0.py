# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        def dfs(i,node):
            if not node:
                return node
            if i==len(res):
                res.append([])
            res[i].append(node.val)
            dfs(i+1,node.left)
            dfs(i+1,node.right)
        
        dfs(0,root)

        for i,v in enumerate(res):
            if i & 1:
                res[i]=reversed(res[i])
        return res

        