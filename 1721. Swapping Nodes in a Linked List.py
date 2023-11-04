# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_head = head
        n = 0
        while temp_head:
            n += 1
            temp_head = temp_head.next
        c = 1
        k_b = None
        temp_head = head
        while temp_head:
            if c == k:
                k_b = temp_head
                break
            c += 1
            temp_head = temp_head.next
        c = 1
        temp_head = head
        while temp_head:
            if c == n-k+1:
                temp_head.val, k_b.val = k_b.val, temp_head.val
                break
            c += 1
            temp_head = temp_head.next
        return head
            
