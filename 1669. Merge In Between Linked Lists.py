# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        ans = list1
        a_prev, b_next = None, None
        while list1:
            if count == a-1:
                a_prev = list1
            if count == b+1:
                b_next = list1
            count += 1
            list1 = list1.next
        a_prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = b_next
        return ans
