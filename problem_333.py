from typing import Tuple
'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NodeStats(object):
    def __init__(self, bst_size: int, is_bst: bool):
        self.bst_size = bst_size
        self.is_bst = is_bst
        self.min = None
        self.max = None

    def update_min_max(self, val: int):
        if val is None:
            return
        if self.min is None:
            self.min = val
        if self.max is None:
            self.max = val
        if val < self.min:
            self.min = val
        if val > self.max:
            self.max = val


class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stats = self.get_largest_bst_size_using_status(root)
        return stats.bst_size

    @classmethod
    def get_largest_bst_size_using_status(cls, node: TreeNode) -> NodeStats:
        # Base cases
        if node is None:
            return NodeStats(0, True)
        if node.left is None and node.right is None:
            stats = NodeStats(1, True)
            stats.update_min_max(node.val)
            stats.min = node.val
            stats.max = node.val
            return stats

        left_stats = cls.get_largest_bst_size_using_status(node.left)
        right_stats = cls.get_largest_bst_size_using_status(node.right)

        max_size_seen = max(left_stats.bst_size, right_stats.bst_size)
        stats = NodeStats(max_size_seen, left_stats.is_bst and right_stats.is_bst)
        stats.update_min_max(left_stats.min)
        stats.update_min_max(left_stats.max)
        stats.update_min_max(right_stats.min)
        stats.update_min_max(right_stats.max)

        if not stats.is_bst:
            return stats

        if node.left and left_stats.max >= node.val:
            stats.is_bst = False
            return stats
        if node.right and right_stats.min <= node.val:
            stats.is_bst = False
            return stats

        stats.bst_size = left_stats.bst_size + right_stats.bst_size
        stats.update_min_max(node.val)
        stats.bst_size += 1
        return stats

