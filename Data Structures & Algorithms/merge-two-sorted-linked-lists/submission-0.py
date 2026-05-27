# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val < list2.val:
            head = list1
            if list1.next == None:
                list1.next = list2
                return head
            l1 = list1.next
            l2 = list2
        else:
            head = list2
            if list2.next == None:
                list2.next = list1
                return head
            l2 = list2.next
            l1 = list1

        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        if l1 == None:
            curr.next = l2
        else:
            curr.next = l1
        return head

