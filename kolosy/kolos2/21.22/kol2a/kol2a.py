from queue import PriorityQueue

from kol2atesty import runtests

def bin_search(arr: list[int], target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def orig_to_node(node_to_orig, orig):
    return bin_search(node_to_orig, orig)

def best_path(zmiany: list[tuple[int,int,int]])->list[int]:
    m = len(zmiany)
    map_arr = [z[1] for z in zmiany]

    # add graph edges

    # edge[0->1] is for Jacek driving, edge[1->0] is for Marian driving - the first one is cost 0
    edges = [([],[]) for _ in range(m)]
    for i in range(m):
        node = i
        cost_m = 0
        for j in range(1,4):
            if i + j < m:
                # target_node = map_arr[i+j]
                _,_,cost = zmiany[i+j]
                cost_m += cost
                edges[node][1].append((i+j, 0))
                edges[node][0].append((i+j, cost_m))

    parent = [[-1 for _ in range(m)] for _ in range(2)]
    visited = [[False for _ in range(m)] for _ in range(2)]
    q = PriorityQueue()
    # cost, node, who is driving (X->other), parent
    q.put((0,0,1,0))
    while not q.empty():
        cost, curr, who, p = q.get()
        if curr == m-1:
            parent[who][curr] = p
            prev_who = 1 - who
            res = []
            while p > 0:
                res.append(map_arr[p])
                next_prev = parent[prev_who][p]
                prev_who = 1 - prev_who
                p = next_prev
            res.reverse()
            return res

        if visited[who][curr]:
            continue

        parent[who][curr] = p
        visited[who][curr] = True

        for v,c in edges[curr][who]:
            q.put((cost+c, v, 1-who, curr))

    return []


def drivers( P: list[tuple[int,bool]], B: int)->list[int]:
    P_with_idx = [(P[i][0],P[i][1], i) for i in range(len(P))]
    arr = sorted(P_with_idx) # nlogn
    n = len(P)
    zmiany = [(0,0,0)]
    i = 0
    curr_check = 0
    while i < n:
        point = arr[i]
        if point[1] == False:
            curr_check += 1
        else:
            zmiany.append((point[0], point[2], curr_check))
            curr_check = 0
        i += 1
    zmiany.append((B, -1, curr_check))



    res = best_path(zmiany)
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )