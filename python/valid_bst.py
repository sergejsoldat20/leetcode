# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        stack = []
        current_node = root

        # pratimo koji je zadnji element i idemo inorder
        last_element = None

        while current_node != None or len(stack) > 0:
            while current_node != None:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            if last_element != None:
                # u slucaju da zadnji element koji skinemo sa steka ima vecu vrijednost nego sledeci onda vracamo false
                if last_element >= current_node.val:
                    return False
                else:
                    last_element = current_node.val
            else:
                last_element = current_node.val

            current_node = current_node.right

        return True


node = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

sol = Solution()

sol.isValidBST(node)
