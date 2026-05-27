class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return head
        l, r = head, head
        i = 0
        while i < n:
            r = r.next
            i += 1
            if r is None:
                return head.next
        
        while r.next:
            l = l.next
            r = r.next
           
        
        l.next = l.next.next
    
        return head