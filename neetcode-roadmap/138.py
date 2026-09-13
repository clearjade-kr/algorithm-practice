from typing import Optional

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        map_nodes = {}

        curr = head
        while curr:
            map_nodes[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            map_nodes[curr].next = map_nodes.get(curr.next)
            map_nodes[curr].random = map_nodes.get(curr.random)
            curr = curr.next

        return map_nodes[head]
