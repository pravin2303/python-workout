

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy  # pointer to build the new list

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # move forward in merged list

        # If any list still has nodes, attach them
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next  # skip dummy head, return actual merged list
