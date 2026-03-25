import sys
from functools import reduce


def radix_sort(T: list[tuple[int,int]])->list[tuple[int,int]]:
    n = len(T)
    biggest = max([t[0] for t in T])

    helper = [(0,0)]*n
    counts = [0] * 10
    exp = 1
    while biggest//exp > 0:
        for i in range(10):
            counts[i] = 0
        for i in range(n):
            counts[(T[i][0]//exp) % 10] += 1
        for i in range(1,10):
            counts[i] += counts[i-1]

        for i in range(n-1,-1,-1):
            counts[(T[i][0]//exp) % 10] -= 1
            helper[counts[(T[i][0]//exp) % 10]] = T[i]
        for i in range(n):
            T[i] = helper[i]
        exp *= 10
    return T

def main():
    inp = sys.stdin.read().split()

    if not inp:
        return

    n = int(inp[0])
    t = int(inp[1])

    ev = []

    for i in range(2, len(inp), 2):
        a_i = int(inp[i])
        b_i = int(inp[i + 1])

        ev.append((a_i, 1))
        ev.append((b_i, -1))

    ev = sorted(ev, key=lambda x: x[0])

    high = 0
    max_ind = -1
    curr = 0
    for el in ev:
        curr += el[1]
        if curr > high:
            high = curr
            max_ind = el[0]

    print(high,max_ind)


if __name__ == "__main__":
    main()

