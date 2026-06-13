# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = fast = head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        cur = mid.next
        mid.next = None
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        f_head = head
        s_head = prev

        while f_head and s_head:
            tmp1 = f_head.next
            tmp2 = s_head.next
            f_head.next = s_head
            s_head.next = tmp1
            f_head = tmp1
            s_head = tmp2
        
        