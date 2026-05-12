import sys


def mult_matrix(A,B,mod):
    C = [[0,0,0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def pow_matrix(M, p, mod):
    res = [[1,0,0],
           [0,1,0],
           [0,0,1]]
    base = M

    while p > 0:
        if p % 2 == 1:
            res = mult_matrix(res, base, mod)
        base = mult_matrix(base, base, mod)
        p //= 2

    return res

def a_n(n):
    mod = 67
    if n == 0: return 1 % mod
    if n == 1: return 2 % mod
    if n == 2: return 7 % mod

    T = [[3, 1, -1],
         [1, 0, 0],
         [0, 1, 0]]

    T_pow = pow_matrix(T, n-2, mod)
    V = [7,2,1]

    A_n = (T_pow[0][0] * V[0] + T_pow[0][1] * V[1] + T_pow[0][2] * V[2]) % mod
    return A_n


count = int(sys.stdin.readline().strip())
for _ in range(count):
    n = int(sys.stdin.readline().strip())
    print(a_n(n-1))
