class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l = 0
        curr = head

        while curr:
            l += 1
            curr = curr.next

        target = l - n

        if target == 0:
            return head.next

        i = 0
        curr = head
        prev = None

        while i < target:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next

        return head