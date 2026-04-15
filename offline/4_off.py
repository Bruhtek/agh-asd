import sys
import queue

Path = tuple[int,int] # to, cost


def djikstra(start: int, end: int, G: list[list[Path]])->tuple[list[int], int]: # Visited nodes, then total cost
    n = len(G)
    if start == end:
        return [], 0

    visited = [False] * n
    q = queue.PriorityQueue()
    q.put((1,start)) # curr_cost, curr
    while q.not_empty:
        cost,v = q.get()
        if visited[v]:
            continue
        if v == end:
            return [], cost

        visited[v] = True
        for u,path_cost in G[v]:
            if not visited[u]:
                new_cost = cost * path_cost
                q.put((new_cost, u))

    return [], 1e12


def main():
    n,m,k = [int(x) for x in sys.stdin.readline().split()]

    G: list[list[Path]] = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = [int(x) for x in sys.stdin.readline().split()]
        G[a].append((b,c))
        G[b].append((a,c))

    goals: list[int] = []
    for _ in range(k):
        goals.append(int(sys.stdin.readline()))

    for g in goals:
        visited,cost = djikstra(1, g, G)
        print(visited, cost)

if __name__ == "__main__":
    main()


# sample data:
# 4 5 2
# 1 2 5
# 1 3 2
# 1 4 8
# 2 3 2
# 3 4 50
# 2
# 4