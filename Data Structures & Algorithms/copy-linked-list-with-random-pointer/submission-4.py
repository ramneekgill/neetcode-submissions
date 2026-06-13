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
        if head is None:
            return None
        hm = {}
        cur = head
        while cur:
            node = Node(cur.val)
            hm[cur] = node
            cur = cur.next
        
        for node in hm:
            if node.next == None:
                hm[node].next = None
            else: 
                hm[node].next = hm[node.next]
            
            if node.random == None:
                hm[node].random = None
            else:
                hm[node].random = hm[node.random]

        return hm[head]
        