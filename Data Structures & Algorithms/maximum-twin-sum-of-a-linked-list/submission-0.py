# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp 
        first, second = head, prev
        res = 0 
        while second:
            temp1, temp2 = first.next, second.next
            res = max(first.val + second.val, res)
            first, second = temp1, temp2

        return res