# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        curr = second
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # now you have two lists where
        # head1 list is shorter than head2 list

        l1 = head
        l2 = prev

        while l1 and l2:
            n1 = l1.next
            n2 = l2.next

            l1.next = l2

            if not n1:
                break

            l2.next = n1

            l1 = n1
            l2 = n2