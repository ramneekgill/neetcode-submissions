# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        preHead = ListNode(-1)
        preHead.next = head
        prev = tail = preHead

        for i in range(n):
            tail = tail.next
        
        while tail.next:
            prev = prev.next
            tail = tail.next
        
        prev.next = prev.next.next

        return preHead.next
            

        