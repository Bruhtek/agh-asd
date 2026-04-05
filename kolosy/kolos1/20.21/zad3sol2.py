
type Range = tuple[int,int,float]

def SortTab(T: list[float], P: list[Range]):
    max_val = max([r[1] for r in P])
    min_val = min([r[0] for r in P])

    n = len(T)
    buckets = [[] for _ in range(n)]
    density = [0 for _ in range(min_val, max_val + 1)]
    for start,end,prob in P:
        avg = prob / (end-start)
        for x in range(start-min_val, end+1-min_val):
            density[x] += avg


    buckets_per_int = [0 for _ in density]
    for i in range(len(density)):
        buckets_per_int[i] = int(density[i] * n) + 1 # expected count of elements inside any given range, +1 to ensure there are no 0s

    bucket_offsets = [d for d in buckets_per_int]
    for i in range(1, len(bucket_offsets)):
        bucket_offsets[i] += bucket_offsets[i-1]

    total_buckets = bucket_offsets[-1]

    print(density, buckets_per_int, bucket_offsets, total_buckets)
    buckets = [[] for _ in range(total_buckets)]




P = [(1,5,0.75), (4,8,0.25)]
T = [6.1, 1.5, 1.2, 3.5, 4.5, 2.5, 3.9, 7.8]
SortTab(T,P)
print(T)