import sys
from collections import deque

inp = sys.stdin.read().split()
P,n,A,B,C = [int(x) for x in inp[0:5]]

nodes = [(int(inp[2*i+5]),int(inp[2*i+6])) for i in range(n)]
nodes.append((P, 0))

nodes.sort(key=lambda x: x[0])

start_idx = -1
for i, (x, e) in enumerate(nodes):
    if x == 0:
        start_idx = i
        break


def dist(d: int)->int:
    return A * d * d + B * d + C


def solve():
    q = deque([(start_idx, nodes[start_idx][1], 0)])
    best_energy = [-1] * (n+1)

    while len(q) > 0:
        idx, energy, jumps = q.popleft()
        pos = nodes[idx][0]

        if best_energy[idx] > energy:
            continue

        best_energy[idx] = energy

        i = idx + 1
        while i <= n:
            next_pos, next_bonus = nodes[i]
            cost = dist(next_pos - pos)

            if cost > energy:
                break

            if best_energy[i] < energy - cost + next_bonus:
                if next_pos == P:
                    return jumps + 1
                q.append((i, energy - cost + next_bonus, jumps + 1))

            i += 1

    return -1

print(solve())