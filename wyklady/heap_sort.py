def parent(i): return (i-1)//2
def left(i): return i*2 + 1
def right(i): return i*2 + 2

# Fix heap O(logn)
def heapify(A: list[int], n: int, i: int):
    max_ind = i
    if left(i) < n and A[left(i)] > A[max_ind]:
        max_ind = left(i)
    if right(i) < n and A[right(i)] > A[max_ind]:
        max_ind = right(i)

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


# Despite looking like O(n*logn), it's actually linear O(n)
def build_heap(A: list[int]):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

# O(nlogn)
def heap_sort(A: list[int]):
    build_heap(A)
    n = len(A)
    for i in range(n-1):
        A[0], A[n-i-1] = A[n-i-1], A[0]
        heapify(A, n-i-1, 0) # log n