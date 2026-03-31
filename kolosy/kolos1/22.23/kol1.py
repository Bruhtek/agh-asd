from kol1testy import runtests

def parent(i: int)->int:
    return (i-1)//2
def left(i: int)->int:
    return i*2 + 1
def right(i: int)->int:
    return i*2 + 2

# Fix the heap O(p)
def heapify(heap: list[tuple[int,int]], i: int):
    l = left(i)
    r = right(i)
    smallest = i
    n = len(heap)
    if l < n and heap[l][0] < heap[i][0]:
        smallest = l
    if r < n and heap[r][0] < heap[smallest][0]:
        smallest = r

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(heap, smallest)

def push(heap: list[tuple[int,int]], val: tuple[int,int]):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        p = parent(i)
        if heap[i][0] < heap[p][0]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break

def pop(heap: list[tuple[int,int]]):
    if len(heap) == 1:
        return heap.pop()

    res = heap[0]
    heap[0] = heap.pop()
    heapify(heap, 0)
    return res

def ksum(T: list[int], k: int, p: int)->int:
    n = len(T)
    if p == 0 or k == 0 or k > p:
        return 0

    min_heap = []
    max_heap = []
    in_min_heap = [-1] * n # shows in which heap each number currently is
    valid_min = 0
    valid_max = 0

    def get_valid(heap, limit: int):
        while len(heap) > 0 and heap[0][1] <= limit:
            pop(heap) # remove leftover elements
        return heap[0] if heap else None

    def pop_valid(heap, limit: int):
        get_valid(heap, limit)
        return pop(heap) if heap else None

    total_sum = 0
    for i in range(n):
        limit = i - p
        if valid_min < k:
            push(min_heap, (T[i], i))
            in_min_heap[i] = 1
            valid_min += 1
        else:
            top_min = get_valid(min_heap, limit)
            if T[i] >= top_min[0]:
                push(min_heap, (T[i], i))
                in_min_heap[i] = 1
                valid_min += 1
            else:
                push(max_heap, (-T[i], i)) #Minus to have the largest element at the top
                in_min_heap[i] = 0
                valid_max += 1

        if i >= p:
            idx = i-p
            if in_min_heap[idx] == 1:
                valid_min -= 1
            else:
                valid_max -= 1

        while valid_min < k and valid_max > 0:
            top_max = pop_valid(max_heap, limit)
            push(min_heap, (-top_max[0], top_max[1]))
            in_min_heap[top_max[1]] = 1
            valid_min += 1
            valid_max -= 1
        while valid_min > k:
            top_min = pop_valid(min_heap, limit)
            push(max_heap, (-top_min[0], top_min[1]))
            in_min_heap[top_min[1]] = 0
            valid_min -= 1
            valid_max += 1

        if i >= p - 1:
            kth = get_valid(min_heap, limit)
            total_sum += kth[0]

    return total_sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
