# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current_node = head
        last_m_node = head

        while current_node is not None:
            # initialize m_count to m and n_count to n
            m_count, n_count = m, n

            # traverse m nodes
            while current_node is not None and m_count != 0:
                last_m_node = current_node
                current_node = current_node.next
                m_count -= 1

            # traverse n nodes
            while current_node is not None and n_count != 0:
                current_node = current_node.next
                n_count -= 1

            # delete n nodes
            last_m_node.next = current_node

        return head