# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def inorderSuccessor(self, root, p):
        current_node = root
        result_list = []
        stack = []
        # true_last_element = False

        while current_node != None or len(stack) > 0:
            while current_node != None:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            result_list.append(current_node)
            if len(result_list) >= 2 and result_list[-2].val == p.val:
                return result_list[-1].val
            current_node = current_node.right
        return None


node = TreeNode(2, TreeNode(1), TreeNode(3))
sol = Solution()
print(sol.inorderSuccessor(node, TreeNode(1)
                           ))
