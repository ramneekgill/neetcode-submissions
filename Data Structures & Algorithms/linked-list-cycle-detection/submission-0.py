# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head.next
        while fast_ptr and fast_ptr.next:
            if slow_ptr == fast_ptr:
                return True
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return False
        