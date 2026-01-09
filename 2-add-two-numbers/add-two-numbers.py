class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        count1 = ""
        while head is not None:
            count1 += str(head.val)
            head = head.next
        count1 = int(count1[::-1])

        head = l2
        count2 = ""
        while head is not None:
            count2 += str(head.val)
            head = head.next
        count2 = int(count2[::-1])

        result = count1+count2
        print(result)
        dummy = ListNode(0)
        curr = dummy

        if result == 0:
            return ListNode(0)

        while result:
            curr.next = ListNode(result % 10)
            curr = curr.next
            result //= 10

        return dummy.next
