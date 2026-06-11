import sys
import queue

Path = tuple[int,int] # to, cost


def calc_routes(start: int, G: list[list[Path]])->list[tuple[list[int], int]]: # Visited nodes, then total cost
    n = len(G)

    visited = [False] * n
    visits = [([], 0) for _ in range(n)] # visited, cost
    q = queue.PriorityQueue()
    q.put((1,start,[])) # curr_cost, curr, list of visited

    while not q.empty():
        cost,v,nodes = q.get()
        if visited[v]:
            continue

        new_nodes = [*nodes, v]
        visited[v] = True
        visits[v] = (new_nodes, cost)

        for u,path_cost in G[v]:
            new_cost = cost * path_cost
            if not visited[u] or (visits[u][1] == new_cost and len(visits[u][0]) > len(new_nodes) + 1):
                q.put((new_cost, u, new_nodes))


    return visits


def main():
    n,m,k = [int(x) for x in sys.stdin.readline().split()]

    G: list[list[Path]] = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = [int(x) for x in sys.stdin.readline().split()]
        G[a].append((b,c))
        G[b].append((a,c))

    visits = calc_routes(1, G)

    for _ in range(k):
        goal = int(sys.stdin.readline())

        route,cost = visits[goal]
        if len(route) == 1:
            print(0, goal, 0)

        print(len(route), end=" ")
        for v in route:
            print(v, end=" ")
        print(cost)



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