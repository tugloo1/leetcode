'''Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NodeStats(object):
    def __init__(self, sum_, tilt):
        self.sum = sum_
        self.tilt = tilt


class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.get_sum_of_subtree(root.left)
        right = self.get_sum_of_subtree(root.right)
        return abs(left - right)

    def get_cum_tilt_of_subtree(self, root: TreeNode):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        full_sum = root.val + self.get_sum_of_subtree(root.left) + self.get_sum_of_subtree(root.right)
        return full_sum
