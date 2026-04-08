# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwo(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        if not A:
            return B
        if not B:
            return A

        guard = ListNode()
        head = guard
        while A is not None and B is not None:
            if A.val < B.val:
                guard.next = A
                guard = guard.next
                A = A.next
            else:
                guard.next = B
                guard = guard.next
                B = B.next

        if A is not None:
            guard.next = A
        else:
            guard.next = B

        return head.next

    def merge_k(self, lists, s, e):
        if e - s == 0:
            return lists[s]
        if e - s == 1:
            return self.mergeTwo(lists[s], lists[e])

        q = (s + e) // 2
        return self.mergeTwo(self.merge_k(lists, s, q), self.merge_k(lists, q + 1, e))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        return self.merge_k(lists, 0, n - 1)
