type Range = tuple[int,int,float]

def insert_sort(T: list[float]):
    i = 1
    n = len(T)
    while i < n:
        j = i
        while j > 0 and T[j-1] > T[j]:
            T[j], T[j-1] = T[j-1], T[j]
            j -= 1
        i += 1

def SortTab(T: list[float], P: list[Range]):
    max_val = max([r[1] for r in P])
    min_val = min([r[0] for r in P])

    buckets_whole = [[] for _ in range(min_val, max_val + 1)]
    for x in T: # O(n)
        ind = int(x) - min_val
        buckets_whole[ind].append(x)


    for bucket in buckets_whole:
        m = len(bucket)
        if m == 0:
            continue

        buckets_parts = [[] for _ in range(m)]
        for x in bucket:
            ind = int((x - int(x)) * m)
            buckets_parts[ind].append(x)

        for buck in buckets_parts:
            insert_sort(buck)

        i = 0
        for buck in buckets_parts:
            for x in buck:
                bucket[i] = x
                i += 1

    i = 0
    for bucket in buckets_whole:
        for x in bucket:
            T[i] = x
            i += 1


P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.5, 1.2, 3.5, 4.5, 2.5, 3.9, 7.8]
SortTab(T,P)
print(T)