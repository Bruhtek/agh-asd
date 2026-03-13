# Merges an array that has two subsets that are sorted into a single sorted part
# A - has two subsets that are sorted
# p - start of subset 1
# q - start of subset 2 (and end of subset 1)
# r - end of subset 2
def merge(A: list[int], B: list[int], p: int, q: int, r: int)->None:
    i = p
    k = p
    j = q

    print("Merging", [A[x] for x in range(p, q)], [A[x] for x in range(q, r)])

    while i < q and j < r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i < q:
        B[k] = A[i]
        i += 1
        k += 1

    while j < r:
        B[k] = A[j]
        j += 1
        k += 1

    for t in range(p, r):
        A[t] = B[t]

def merge_sort(A: list[int], B: list[int], p: int, r: int)->None:
    if r - p <= 1:
        return

    print("Sorting", [A[x] for x in range(p, r)])

    q = (r + p) // 2
    merge_sort(A, B, p, q)
    merge_sort(A, B, q, r)

    merge(A, B, p, q, r)


def msort(A: list[int]):
    n = len(A)
    B = [0] * n

    merge_sort(A, B, 0, n)



tab = [5,1,13,15,4,7,9,5]
msort(tab)
print(tab)