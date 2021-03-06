# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        def helper(root, level):
            if root is None:
                pass
            else:
                if len(queue) <= level:
                    queue.append([])
                queue[level].append(root.val)
                helper(root.left, level+1)
                helper(root.right, level+1)
        helper(root, 0)
        return queue
