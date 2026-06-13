# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre_head = ListNode(-1,head)
        first_ptr = head
        for x in range(n):
            first_ptr = first_ptr.next
        second_ptr = pre_head
        while first_ptr:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        second_ptr.next = second_ptr.next.next
        return pre_head.next



        