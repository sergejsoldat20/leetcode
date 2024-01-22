class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def print_linked_list(self, head):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

    def reverseList(self, head):
        current_node = head
        is_first = True
        new_head = ListNode()
        while current_node != None:

            new_node = ListNode()
            new_node.val = current_node.val
            # print(new_node.val)
            if is_first:
                new_node.next = None
                is_first = False
            else:
                new_node.next = new_head.next
            new_head.next = new_node

            current_node = current_node.next

        return new_head.next


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link nodes
node1.next = node2
node2.next = node3

sol = Solution()
sol.print_linked_list(sol.reverseList(node1))
