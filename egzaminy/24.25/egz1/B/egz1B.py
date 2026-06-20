from collections import deque

from egz1Btesty import runtests
from math import inf as INF

def topo_sort(G: list[list[int]], E: list[tuple[int,int]], n)->list[int]:
    inc_count = [0] * n
    for _,v in E:
        inc_count[v] += 1

    q = deque([])
    for i in range(n):
        if inc_count[i] == 0:
            q.append(i)

    res = []
    while len(q) > 0:
        v = q.popleft()
        res.append(v)
        for u in G[v]:
            inc_count[u] -= 1
            if inc_count[u] == 0:
                q.append(u)
    return res

def E_to_G(V: int, E: list[tuple[int,int]]):
    G = [[] for _ in range(V)]
    for u,v in E:
        G[u].append(v)
    return G

def critical(V, E):
    G = E_to_G(V, E)
    order = topo_sort(G,E,V)
    print(order)
    v_to_order = {v: i for i, v in enumerate(order)}

    res = 0
    for v in range(V):
        neigh = G[v]
        neigh.sort(key=lambda x: v_to_order[x])

        visited = [False] * V
        for v in neigh:
            if not visited[v]:
                res += 1
                stack = [v]
                while stack:
                    curr = stack.pop()
                    for u in G[curr]:
                        if not visited[u]:
                            visited[u] = True
                            stack.append(u)

    return res
        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)

    
