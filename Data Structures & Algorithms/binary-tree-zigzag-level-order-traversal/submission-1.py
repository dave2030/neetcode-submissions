# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        # def dfs(i,node):
        #     if not node:
        #         return node
        #     if i==len(res):
        #         res.append([])
        #     res[i].append(node.val)
        #     dfs(i+1,node.left)
        #     dfs(i+1,node.right)
        
        # dfs(0,root)

        # for i,v in enumerate(res):
        #     if i %2==1:
        #         res[i]=reversed(res[i])
        # return res
        q=deque([root])
        res=[]
        cnt=0
        while q:
            level=[]
            for x in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if cnt & 1:
                    res.append(reversed(level))
                else:
                    res.append(level)
            cnt+=1
        return res


        