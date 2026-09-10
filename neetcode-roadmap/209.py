from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        next_node = head

        while next_node:
            next_target = next_node.next
            next_node.next = prev_node
            prev_node, next_node = next_node, next_target

        return prev_node


if __name__ == "__main__":
    sol = Solution()
    node_5 = ListNode(val=5)
    node_4 = ListNode(val=4, next=node_5)
    node_3 = ListNode(val=3, next=node_4)
    node_2 = ListNode(val=2, next=node_3)
    node_1 = ListNode(val=1, next=node_2)

    print(sol.reverseList(head=node_1))
