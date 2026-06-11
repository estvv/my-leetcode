class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        self.reverseN(head, 1, 3)

    def reverseN(self, head: ListNode, start: int, stop: int):
        if not head or start == stop:
            return head
        left_prev = head
        curr = head

        for _ in range(start - 1):
            left_prev = left_prev.next
            curr = curr.next
        prev = None
        for _ in range(stop - start + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left_prev.next = prev

        print(head)

Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3))), 2)
