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
            if not (p and q):
                return False

            if p.val != q.val:
                return False

            if not (p.left or p.right or q.left or q.right):
                return p.val == q.val

            return is_same(p.left, q.left) and is_same(p.right, q.right)

        ret_flag = False
        def check_tree(node):
            nonlocal ret_flag
            if ret_flag:
                return
            if is_same(node, subRoot):
                ret_flag = True
                return
            if node.left:
                check_tree(node.left)
            if node.right:
                check_tree(node.right)

        check_tree(root)
        return ret_flag

