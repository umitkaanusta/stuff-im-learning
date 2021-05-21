class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # first: reverse one side
        # then compare each side 
        # O(n) time, O(1) space
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if length == 1:
            return True
        mid = length // 2
        second_part = mid if length % 2 == 0 else mid + 1
        i = head
        j = head
        for _ in range(second_part):
            j = j.next
        j = self.reversePart(j)
        while j:
            if i.val == j.val:
                i = i.next
                j = j.next
            else:
                return False
        return True
            
    def reversePart(self, head: ListNode):
        prev = None
        curr = head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        head = prev
        return head
