# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_l1 = [] 
        list_l2 = []
        while l1:
            list_l1.append(l1.val)
            l1 = l1.next
        while l2:
            list_l2.append(l2.val)
            l2 = l2.next
        list_l1.reverse()
        list_l1 = self.list_to_number(list_l1)
        list_l2.reverse()
        list_l2 = self.list_to_number(list_l2)
        list_l1 = list_l1 + list_l2
        list_l1 = str(list_l1)[::-1]
        list_l1 = self.number_to_list(list_l1)
        lr = ListNode(val = list_l1[0], next = None)
        temp = lr
        for i in range(1, len(list_l1)):
            lr.next = ListNode(val = list_l1[i], next = None)
            lr = lr.next
        return temp

    def list_to_number(self, lst):
        return int(''.join(map(str, lst)))

    def number_to_list(self, num):
        return [int(digit) for digit in str(num)]
