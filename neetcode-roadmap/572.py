# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:        

        def is_same(p, q):
            if not (p or q):
                return True

            if not p or not q or p.val != q.val:
                return False

            return is_same(p.left, q.left) and is_same(p.right, q.right)

        
        if not root:
            return False

        if is_same(root, subRoot):
            return True

        return self.isSubtree(root=root.left, subRoot=subRoot) or self.isSubtree(root=root.right, subRoot=subRoot)

