# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memo =  []
        while headA or headB:
            if headA and headA in memo:
                return headA
            elif headA:
                memo.append(headA)
                headA = headA.next
            if headB and headB in memo:
                return headB
            elif headB:
                memo.append(headB)
                headB = headB.next
        return None
