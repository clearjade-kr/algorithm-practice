from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Save in list and calculate next node index
        
        node_list = []
        next_node = head
        while next_node:
            node_list.append(next_node)
            next_node = next_node.next

        N = len(node_list)
        for i in range(N // 2):
            node_list[i].next = node_list[N - 1 - i]
            node_list[N - 1 - i].next = node_list[i + 1]
        node_list[N // 2].next = None
        
        # target_node = head
        # while target_node:
        #     print(target_node.val)
        #     target_node = target_node.next

        
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

