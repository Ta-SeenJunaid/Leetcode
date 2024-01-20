class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even_head = even = head.next

        # This condition makes sure odd can never be None, since the odd node will always be the one before the even node.
        # If even is not None, then odd is not None. (odd before even)
        # If even.next is not None, then after we update odd to the next odd node, it cannot be None. (The next odd node is even.next)
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even=even.next

        odd.next = even_head
        return head
