from collections import deque

from kol3testy import runtests


def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])

    # y,x,cost
    q = deque([(0,0,0)])
    while len(q) > 0:
        y,x,cost = q.popleft()
        curr_s = C[y][x]
        if curr_s == -1:
            continue

        C[y][x] = -1 #używam istniejącej tablicy, aby uniknąć alokacji nowej, kosztującej n*m
        right_s = C[y][x+1] if x < m-1 else float('-inf')
        down_s = C[y+1][x] if y < n-1 else float('-inf')

        if (x == m-1 or y == n-1) and curr_s <= s:
            return cost

        if curr_s - down_s <= s:
            q.append((y+1, x, cost+1))
        if curr_s - right_s <= s:
            q.append((y, x+1, cost+1))

    return -1

runtests(parkiet, all_tests = True)
