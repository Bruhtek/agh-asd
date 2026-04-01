# Wersja Lomuto - łatwiejsza do implementacji, ale wolniejsza
def partition(A: list[int], p: int, r: int):
    x = A[r]
    i = p-1
    for j in range(p, r+1):
        if A[j] > x:
            continue

        i += 1
        A[i], A[j] = A[j], A[i] # swap

    return i


def qsort(A: list[int], p: int, r: int):
    if not p < r:
        return

    q = partition(A, p, r)
    qsort(A, p, q-1)
    qsort(A, q+1, r)



# Mniej odstawiane na stos
def better_qsort(A: list[int], p: int, r: int):
    while p < r:
        q = partition(A, p, r)
        better_qsort(A, p, q-1)
        p = q+1

# Uses maximally O(logn) on the stack
def even_better_qsort(A: list[int], p: int, r: int):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            even_better_qsort(A, p, q-1)
            p = q + 1
        else:
            even_better_qsort(A, q+1, r)
            r = q - 1


tab = [65,213,5,21,5123,754,171,85]
print(tab)
even_better_qsort(tab, 0, len(tab)-1)
print(tab)