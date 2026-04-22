# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0 
        while cur:
            cur = cur.next
            length += 1
        
        cur = head 
        if n == length:
            return head.next

        remainder = length - n 
        while remainder > 1:
            remainder -= 1
            cur = cur.next
        cur.next = cur.next.next
        return head
    


