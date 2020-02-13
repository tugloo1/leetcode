# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 1
        current_layer = [root]
        next_layer = []

        while current_layer:
            for node in current_layer:
                if node.right:
                    next_layer.append(node.right)
                if node.left:
                    next_layer.append(node.left)
            if not next_layer:
                break
            current_layer = next_layer
            next_layer = []
            depth += 1
        return depth

