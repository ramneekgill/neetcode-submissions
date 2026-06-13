"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None: None}
        cur = head
        while cur:
            node = Node(cur.val)
            hm[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            hm[cur].next = hm[cur.next]
            hm[cur].random = hm[cur.random]
            cur = cur.next

        return hm[head]
        