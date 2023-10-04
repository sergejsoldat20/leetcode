class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def popFromList(self, li_list):
        if li_list is not None:
            return li_list.val
        return 0

    def addTwoNumbers(self, l1, l2):
        result_node = ListNode()
        current_node = result_node

        rest = 0

        while l1 or l2:
            l1_value = self.popFromList(l1)
            l2_value = self.popFromList(l2)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            result = l1_value + l2_value + rest

            if result >= 10:
                result = result % 10
                rest = 1
            else:
                rest = 0

            current_node.next = ListNode(result)
            current_node = current_node.next

        if (rest == 1):
            current_node.next = ListNode(rest)

        return result_node.next


sol = Solution()


node = sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(9))),
                         ListNode(5, ListNode(6, ListNode(4, ListNode(9)))))

while node:
    print(node.val)
    node = node.next
