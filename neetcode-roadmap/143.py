from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Finding middle node with two pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Cutting list into half and reversing second half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merging two halves of list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        
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


    sol.reorderList(head = node_1)

