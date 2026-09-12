from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles edge case where the head itself needs to be removed
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Set fast to locate N + 1 to make difference from fast to slow to N + 1
        for _ in range(n + 1):
            fast = fast.next

        # Move fast to the end, with slow maintaining distance to N + 1
        # slow will point the node N + 1 before the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    # node_5 = ListNode(val=5)
    # node_4 = ListNode(val=4, next=node_5)
    # node_3 = ListNode(val=3, next=node_4)
    # node_2 = ListNode(val=2, next=node_3)
    # node_1 = ListNode(val=1, next=node_2)

    node_4 = ListNode(val=4)
    node_3 = ListNode(val=3, next=node_4)
    node_2 = ListNode(val=2, next=node_3)
    node_1 = ListNode(val=1, next=node_2)

    sol.removeNthFromEnd(head=node_1)
