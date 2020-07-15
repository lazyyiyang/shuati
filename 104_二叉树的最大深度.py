# 104 二叉树的最大深度
'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
'''
# dfs思想 最大深度等于最大的子树深度+1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

# bfs思想 运用栈储存子树 若子树存在则深度+1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        stack=[(1,root)]
        depth=0
        dps=0
        while stack!=[]:
            dps,root=stack.pop()
            if root:
                depth=max(depth,dps)
                stack.append((dps+1,root.left))
                stack.append((dps+1,root.right))
        return depth