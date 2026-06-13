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
        ll_dict = {None: None}
        ptr = head
        while ptr:
            ll_dict[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            ll_dict[ptr].next = ll_dict[ptr.next]
            ll_dict[ptr].random = ll_dict[ptr.random]
            ptr = ptr.next
        
        return ll_dict[head]




            
            
            



        

            



            