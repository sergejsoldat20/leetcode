# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#         current_node = node

#         next = current_node.next
#         current_node.val = next.val
#         current_node.next = next.next


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]

        binary = binary.zfill(32)
        print(binary.count('1'))


sol = Solution()
sol.hammingWeight(5)
