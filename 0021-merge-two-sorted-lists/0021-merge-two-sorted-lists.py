class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        ptr = list1
        head = list1
        while head.next is not None:
            head = head.next
        head.next = list2
        swapped = True
        while swapped:
            swapped = False
            ptr = list1
            while ptr and ptr.next:
                if ptr.val > ptr.next.val:
                    ptr.val, ptr.next.val = ptr.next.val, ptr.val
                    swapped = True
                ptr = ptr.next
        return list1