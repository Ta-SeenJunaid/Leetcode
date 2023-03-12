# https://leetcode.com/problems/merge-two-sorted-lists/solutions/3197726/easy-solution-explained-with-illustration-no-waste-of-time/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode()
        pointer = dummy
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        if list1:
                pointer.next = list1
        else:
            pointer.next = list2
        return dummy.next
