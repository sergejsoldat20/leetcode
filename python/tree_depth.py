# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative solution


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0

        while stack != []:
            current_depth, root = stack.pop()
            # skida se node sa dubinom iz stack i onda se dodaju djeca sa + 1 dubinom
            if root is not None:
                # provjeravaju se dubine kod djece i uzima se max
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth


# Recursive solution

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         else:
#             left_height = self.maxDepth(root.left)
#             right_height = self.maxDepth(root.right)
#             return max(left_height, right_height) + 1
