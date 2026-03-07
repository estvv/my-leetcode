# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSameTree(root.left, root.right)

    def isSameTree(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.isSameTree(left.left, right.right) and self.isSameTree(left.right, right.left)
