from queue import Queue
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Assuming t1 and t2 are not None!
        q = Queue()
        # Rules: The queue can not have any nodes with None in it
        q.put((t1, t2))
        while q:
            nodes = q.get()
            if len(nodes) == 2:
                left_tree_node, right_tree_node = nodes
                left_tree_node.val += right_tree_node.val
                # Handling left children
                left_children = (left_tree_node.left, right_tree_node.left)
                filtered = tuple(filter(None, left_children))
                if len(filtered) != 0:
                    q.put(filtered)
                    if len(filtered) == 1:
                        left_tree_node.left = filtered

                # Handling right children
                right_children = (left_tree_node.right, right_tree_node.right)
                filtered = tuple(filter(None, right_children))
                if len(filtered) != 0:
                    q.put(filtered)
                    if len(filtered) == 1:
                        left_tree_node.right = filtered
        return t1


class SolutionTestCase(TestCase):
    def create_tree(self, inp):
        pass