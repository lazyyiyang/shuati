# 对称二叉树
'''
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
'''
# 递归思想
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def same(r1,r2):
            if not r1 and not r2: return True
            if not r1 or not r2:return False
            if r1.val!=r2.val:return False
            return same(r1.left,r2.right) and same(r1.right,r2.left)
        if not root:return True 
        return same(root.left,root.right)
'''
判断二叉树是否对称

若 root == null, 直接返回 true；

否则，判断 root.left 与 root.right 这两棵子树是否对称：

判断 root.left 与 root.right 这两个节点的值是否相等

判断 root.left 的左子树与 root.right 的右子树是否对称

判断 root.left 的右子树与 root.right 的左子树是否对称
'''