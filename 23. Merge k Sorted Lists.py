# https://www.youtube.com/watch?v=q5a5OiGbT6Q
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i+1) < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                temp.append(self.mergeTwoLists(list1, list2))
            lists = temp
        return lists[0]

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
