# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        ret_flag = True

        def check_depth(node):
            nonlocal ret_flag

            if not node:
                return 0

            left_depth = check_depth(node.left)
            right_depth = check_depth(node.right)
            if not ret_flag:
                return

            if left_depth - right_depth > 1 or left_depth - right_depth < -1:
                ret_flag = False

            return max(left_depth, right_depth) + 1

        check_depth(root)
        return ret_flag

