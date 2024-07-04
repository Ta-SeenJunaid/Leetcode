# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modified_list = None
        while head:
            if head.val != 0:
                count = 0
                while head.val != 0:
                    count += head.val
                    head = head.next
                if modified_list:
                    temp = ListNode(val=count)
                    modified_list.next = temp
                    modified_list = modified_list.next
                else:
                    modified_list = ListNode(val=count)
                    ans = modified_list
            head = head.next
        return ans
        
