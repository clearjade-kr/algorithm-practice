from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Check max length for left and right branch
        # Calculate max diameter passing current node and compare

        ret_val = 0

        def get_max_depth(node):
            nonlocal ret_val
            if not node:
                return 0

            left_max_depth = get_max_depth(node.left)
            right_max_depth = get_max_depth(node.right)
            ret_val = max(ret_val, left_max_depth + right_max_depth)

            return max(left_max_depth, right_max_depth) + 1

        get_max_depth(root)
        return ret_val


if __name__ == "__main__":
    sol = Solution()
    node_5 = TreeNode(val=5)
    node_4 = TreeNode(val=4)
    node_3 = TreeNode(val=3)
    node_2 = TreeNode(val=2, left=node_4, right=node_5)
    node_1 = TreeNode(val=1, left=node_2, right=node_3)

    print(sol.diameterOfBinaryTree(root=node_1))
