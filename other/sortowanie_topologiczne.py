from collections import deque


def directed_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
    return G

def topo_sort(G: list[list[int]]):
    n = len(G)
    v_c = [0] * n

    q = deque([])

    for i in range(n):
        for u in G[i]:
            v_c[u] += 1

    for i in range(n):
        if v_c[i] == 0:
            q.append(i)

    res = []
    while len(q) > 0:
        v = q.popleft()
        res.append(v)

        for u in G[v]:
            v_c[u] -= 1
            if v_c[u] == 0:
                q.append(u)
    return res

E = [(0, 1), (0, 2), (1, 2), (1, 4), (4, 3), (4, 6), (4, 5), (7, 4), (8, 7)]

G = directed_graph_list(E, 9)
print(G)
print(topo_sort(G))