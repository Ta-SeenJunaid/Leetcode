# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        root = head
        count = 0
        while head:
            count += 1
            head = head.next
        change = count - n
        count = 0
        if change == 0:
            return root.next
        head = root
        while head:
            count += 1
            if count == change:
                head.next = head.next.next
                break
            head = head.next
        return root
        
