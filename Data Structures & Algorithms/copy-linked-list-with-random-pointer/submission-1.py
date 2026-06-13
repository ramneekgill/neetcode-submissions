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
        if not head:
            return
        new_list = Node(head.val)
        pre_head = Node(0, new_list)
        curr = head.next
        while curr:
            new_list.next = Node(curr.val)
            curr = curr.next
            new_list = new_list.next
        
        ls_head = pre_head.next
        curr = head
        while ls_head:
            rand = curr.random
            ptr = head
            ls_ptr = pre_head.next
            while ptr != rand:
                ptr = ptr.next
                ls_ptr = ls_ptr.next
            ls_head.random = ls_ptr
            ls_head = ls_head.next
            curr = curr.next
        
        return pre_head.next
            
            
            



        

            



            