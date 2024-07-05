# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        head = head.next
        count = 1
        first_c_p = None
        last_c_p = None
        mind = None
        maxd = None
        while head and head.next:
            if prev.val > head.val < head.next.val or prev.val < head.val > head.next.val:
                if first_c_p == None:
                    first_c_p = count
                    last_c_p = count
                else:
                    if mind != None:
                        mind = min(count - last_c_p, mind)
                    else:
                        mind = count - last_c_p
                last_c_p = count   
            prev = head
            head = head.next
            count += 1
        maxd = (last_c_p if last_c_p else 0) - (first_c_p if first_c_p else 0)
        return [mind if mind else -1, maxd if maxd else -1]  
        
