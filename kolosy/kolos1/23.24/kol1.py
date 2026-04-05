from kol1testy import runtests

def merge(T: list[list[int]], startA: int, startB: int, end: int):
    k = 0
    i = startA
    j = startB
    helper = [[0,0] for _ in range(end-startA+1)]
    while i < startB and j <= end:
        if T[i][0] < T[j][0]:
            helper[k] = T[j]
            helper[k][1] += startB - i
            j += 1
        else:
            helper[k] = T[i]
            i += 1
        k += 1

    while i < startB:
        helper[k] = T[i]
        i += 1
        k += 1
    while j <= end:
        helper[k] = T[j]
        j += 1
        k += 1

    T[startA:end+1] = helper[0:end-startA+1]


def merge_sort(T: list[list[int]], start: int, end: int):
    if start < end:
        mid = (end + start) // 2
        merge_sort(T, start, mid)
        merge_sort(T, mid+1, end)
        merge(T, start, mid+1, end)


def maxrank(T):
    n = len(T)
    l = [[T[i], 0] for i in range(n)]
    merge_sort(l, 0, n-1)
    return max([x[1] for x in l])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests=True)
