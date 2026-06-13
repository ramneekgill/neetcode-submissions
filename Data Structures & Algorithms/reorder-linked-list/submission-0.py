# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec_list = slow.next
        slow.next = prev = None
        while sec_list:
            tmp = sec_list.next
            sec_list.next = prev
            prev = sec_list
            sec_list = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head

        




        