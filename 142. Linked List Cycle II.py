# https://www.youtube.com/watch?v=gBTe7lFR3vc
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        pointer = head
        while pointer != slow:
            slow = slow.next
            pointer = pointer.next
        return slow