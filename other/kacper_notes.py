# MERGESORT
# Time Complexity: O(n log n) for Best, Average, and Worst cases
# Space Complexity: O(n)
# Stable: Yes
# In-place: No


def merge(arr, buf, l, m, r):
    i = l  # left half
    j = m + 1  # right half
    k = l  # buffer (buf)
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            buf[k] = arr[i]
            i += 1
        else:
            buf[k] = arr[j]
            j += 1
        k += 1
    while i <= m:
        buf[k] = arr[i]
        i += 1
        k += 1
    while j <= r:
        buf[k] = arr[j]
        j += 1
        k += 1
    arr[l:r+1] = buf[l:r+1]


def mergesort(arr, buf, l, r):
    if l < r:
        m = (l + r) // 2
        mergesort(arr, buf, l, m)
        mergesort(arr, buf, m + 1, r)
        merge(arr, buf, l, m, r)


def run_mergesort(arr):
    buf = [0] * len(arr)
    mergesort(arr, buf, 0, len(arr) - 1)


# HEAPSORT
# Time Complexity: O(n log n) for Best, Average, and Worst cases
# Space Complexity: O(1) (Actually this implementation is O(log n), because of recursive heapify)
# Stable: No
# In-place: Yes


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heapify(arr, n, i):
    largest = i
    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, n, i)


def heapsort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n - 1):
        arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]
        heapify(arr, n - i - 1, 0)


# QUICKSORT
# Time Complexity: Best: O(n log n), Average: O(n log n), Worst: O(n^2)
# Space Complexity: O(log n)
# Stable: No
# In-place: Yes


def partition(A, l, r):
    pivot = A[r]
    p = l
    for i in range(l, r + 1):
        if A[i] > pivot:
            continue
        A[p], A[i] = A[i], A[p]
        p += 1
    return p - 1


# def quicksort(A, l, r):
#     if l < r:
#         p = partition(A, l, r)
#         quicksort(A, l, p - 1)
#         quicksort(A, p + 1, r)


# manual tail call optimization
def quicksort(A, l, r):
    while l < r:
        p = partition(A, l, r)
        quicksort(A, l, p - 1)
        l = p + 1

# COUNTING SORT
# Time Complexity: O(n + k) where k is the range of the input
# Space Complexity: O(n + k)
# Stable: Yes
# In-place: No


def countingsort(A):
    max_value = max(A)
    counters = [0] * (max_value + 1)
    for value in A:
        counters[value] += 1
    print(counters)
    for i in range(1, len(counters)):
        counters[i] += counters[i - 1]
    out = [0] * len(A)
    print(counters)
    for value in reversed(A):
        counters[value] -= 1
        i = counters[value]
        out[i] = value
    return out


# BUCKET SORT
# Time Complexity: Average: O(n + k), Worst: O(n^2) (depends on underlying sort)
# Space Complexity: O(n + k)
# Stable: Yes
# In-place: No

# FOR SORTING VALUES [0, 1) ONLY
def bucketsort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    for value in A:
        buckets[int(value * n)].append(value)
    for bucket in buckets:
        bucket.sort()
    i = 0
    for bucket in buckets:
        for value in bucket:
            A[i] = value
            i += 1
