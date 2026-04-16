import sys
import queue

Path = tuple[int,int] # to, cost


def calc_routes(start: int, G: list[list[Path]])->list[tuple[int|None, int, int]]: # Visited nodes, then total cost
    n = len(G)

    visited = [False] * n
    visits = [(None, 0, 0) for _ in range(n)] # parent, len, cost
    q = queue.PriorityQueue()
    q.put((1,0,start,None)) # curr_cost, curr_len, curr, parent

    while not q.empty():
        cost,path_len,v,parent = q.get()
        if visited[v]:
            continue

        visited[v] = True
        visits[v] = (parent, path_len+1, cost)

        for u,path_cost in G[v]:
            new_cost = cost * path_cost
            if not visited[u]:
                q.put((new_cost, path_len + 1, u, v))


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

        parent,route_len,cost = visits[goal]
        route = [0 for _ in range(route_len)]
        route[route_len-1] = goal
        for i in range(route_len-2, -1, -1):
            route[i] = parent
            parent,_,__ = visits[parent]


        print(route_len, end=" ")
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