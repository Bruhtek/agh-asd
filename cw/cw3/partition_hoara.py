def partition(A: list[int], p: int, r: int):
    pivot = A[r]
    s = p
    k = r - 1
    while True:
        while A[s] < pivot:
            s += 1

        while A[k] > pivot:
            k -= 1

        if s < k:
            A[s], A[k] = A[k], A[s]
        else:
            return k