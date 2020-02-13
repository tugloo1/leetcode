from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        _, balanced = self.get_height_and_balanced_status(root)
        return balanced

    def get_height_and_balanced_status(self, node: TreeNode) -> [int, bool]:
        if node.left is None and node.right is None:
            return 1, True
        l_h, r_h, l_s, r_s = 0, 0, True, True
        if node.left:
            l_h, l_s = self.get_height_and_balanced_status(node.left)
        if node.right:
            r_h, r_s = self.get_height_and_balanced_status(node.right)

        height = max(l_h, r_h) + 1
        balanced = l_s and r_s
        if balanced and abs(l_h - r_h) > 1:
            balanced = False
        return height, balanced

