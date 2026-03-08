# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []

        self.dfs(res, root)

        return res

    def dfs(self, res, node: TreeNode):
        if not node:
            return

        self.dfs(node.left)
        res.append(node.val)
        self.dfs(node.right)
