import sys
from collections import deque

Path = tuple[int,int] # to, cost


def dfs(start: int, end: int, G: list[list[Path]])->tuple[list[int], int]: # Visited nodes, then total cost
    n = len(G)



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

    print(G, goals)

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