import array
import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    A = int(data[2])
    B = int(data[3])
    q = int(data[4])

    queries = []
    idx = 5
    max_req = 2
    for _ in range(q):
        k = int(data[idx])
        x = int(data[idx+1])
        y = int(data[idx+2])
        queries.append((k, x, y))

        Dx = max(0, x - 1)
        Dy = max(0, y - 1)
        req = max(Dx, Dy) + k + 2
        if req > max_req:
            max_req = req

        idx += 3

    p = 1_000_696_969

    MAX_REQ = max_req

    fact = array.array('I', [1] * MAX_REQ)
    for i in range(1, MAX_REQ):
        fact[i] = (fact[i - 1] * i) % p

    inv_fact = array.array('I', [1] * MAX_REQ)
    inv_fact[MAX_REQ - 1] = pow(fact[MAX_REQ - 1], p - 2, p)
    for i in range(MAX_REQ - 2, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % p

    def nCr(n_val, k_val):
        if k_val < 0 or k_val > n_val:
            return 0
        return (fact[n_val] * inv_fact[k_val] % p) * inv_fact[n_val - k_val] % p

    def solve_axis(D, S, k):
        if D < 0:
            return 0
        if k == 0:
            return 1 if D == 0 else 0

        limit = min(k, D // S)
        ans = 0

        for j in range(limit + 1):
            term = (nCr(k, j) * nCr(D - j * S + k - 1, k - 1)) % p
            if j % 2 == 1:
                ans = (ans - term + p) % p
            else:
                ans = (ans + term) % p
        return ans


    for k, x, y in queries:
        if x == 0 or y == 0:
            print("0")

        dx = x - 1
        dy = y - 1

        wx = solve_axis(dx, A + 1, k)
        wy = solve_axis(dy, B + 1, k)

        res = (wx * wy) % p
        print(str(res))

solve()