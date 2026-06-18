import sys


def xor_prefix(x: int)->int:
    rem = x % 4
    if rem == 0:
        return x
    if rem == 1:
        return 1
    if rem == 2:
        return x+1
    return 0

def solve(n: int, K: int)->int:
    A = 1 + K
    B = n + K
    total = xor_prefix(B) ^ xor_prefix(A - 1)


    return total - K


if __name__ == "__main__":
    n, k = [int(x) for x in sys.stdin.readline().split()]
    print(solve(n, k))