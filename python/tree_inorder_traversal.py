# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # iterativni nacin
    def inorderTraversal(self, root):
        current_node = root
        stack = []  # samo radi push i pop, Stack je last in first out
        result_list = []
        while current_node != None or len(stack) > 0:
            # vrtimo petlju da ide stablo skroz u lijevu stranu i dodajemo na stack
            while current_node != None:
                stack.append(current_node)
                current_node = current_node.left
            # skidamo sa steka, dodajemo vrijednost i postavimo za sledeci prvi u desno
            current_node = stack.pop()
            result_list.append(current_node.val)
            current_node = current_node.right

        return result_list

    # rekurzivni nacin
    def traversal(self, visited, root):
        if root != None:
            self.traversal(visited, root.left)
            visited.append(root.val)
            self.traversal(visited, root.right)


node = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

sol = Solution()

print(sol.inorderTraversal(node))
