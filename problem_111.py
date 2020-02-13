# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = [root]
        next_queue = []
        min_depth = 1

        while len(q) > 0:
            for node in q:
                if node.left or node.right:
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)
                    continue
                else:
                    return min_depth
            q = next_queue
            next_queue = []
            min_depth += 1
