# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0, head)
        fst = dummy
        snd = dummy

        for _ in range(n + 1):
            snd = snd.next

        while snd is not None:
            fst = fst.next
            snd = snd.next

        fst.next = fst.next.next
        return dummy.next

Solution.removeNthFromEnd(Solution, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
Solution.removeNthFromEnd(Solution, ListNode(1), 1)
Solution.removeNthFromEnd(Solution, ListNode(1, ListNode(2)), 1)


