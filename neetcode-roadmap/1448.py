# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret_val = 0

        # DFS approach with having maximal value

        def dfs(node, cur_max):
            nonlocal ret_val
            if not node:
                return 

            if node.val >= cur_max:
                ret_val += 1
                cur_max = node.val

            dfs(node=node.right, cur_max=cur_max)
            dfs(node=node.left, cur_max=cur_max)

        dfs(node=root, cur_max=root.val)
        return ret_val


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    print(sol.goodNodes(root=root))
