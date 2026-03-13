class Node:
    @staticmethod
    def from_arr(arr: list[int]):
        head = Node(arr[0])
        curr = head
        for i in range(1, len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
        return head

    def __init__(self, val: int, next: "Node" = None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = f"{self.val}"
        curr = self.next
        while curr:
            s += f"-{curr.val}"
            curr = curr.next
        return s

def merge(A: Node, B: Node)->Node:
    if A is None:
        return B
    if B is None:
        return A

    if A.val < B.val:
        head = A
        A = A.next
    else:
        head = B
        B = B.next

    curr = head
    while A is not None and B is not None:
        if A.val < B.val:
            curr.next = A
            A = A.next
        else:
            curr.next = B
            B = B.next

        curr = curr.next

    if A is not None:
        curr.next = A
    else:
        curr.next = B

    return head


def mergesort(t: Node):
    curr = t
    parts = [t]
    while curr.next is not None:
        if curr.next.val < curr.val:
            parts.append(curr.next)
            curr.next = None
            curr = parts[-1]
        else:
            curr = curr.next

    while len(parts) > 1:
        print(parts)
        tmp = []
        for i in range(1, len(parts), 2):
            tmp.append(merge(parts[i-1], parts[i]))
        if len(parts) % 2 != 0:
            tmp.append(parts[-1])

        parts = tmp

    return parts[0]

a = Node.from_arr([1,2,3,8,9])
b = Node.from_arr([0,2,4,4,5,6,7])

print(merge(a, b))

t = Node.from_arr([5,6,8,1,2,7,3,1,2])
print(mergesort(t))