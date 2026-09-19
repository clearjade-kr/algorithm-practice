# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


if __name__ == "__main__":
    sol = Solution()
    node_5 = TreeNode(x=5)
    node_4 = TreeNode(x=4)
    node_3 = TreeNode(x=3)
    node_2 = TreeNode(x=2)
    node_1 = TreeNode(x=1)

    node_4.left = node_2
    node_4.right = node_5
    node_2.left = node_1
    node_2.right = node_3

    sol.lowestCommonAncestor(root=node_4, p=node_1, q=node_5)