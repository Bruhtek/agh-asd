import sys
from random import randint, seed

OIOIOI = True


# def gt(a: str, b: str)->bool:
#     if a == b: return False
#
#     n = len(a)
#     m = len(b)
#
#     i, j = 0, 0
#     while i < n and j < m and a[i] == b[j]:
#         i += 1
#         j += 1
#
#     if i == n:
#         return False
#     elif j == m:
#         return True
#
#     return ord(a[i]) > ord(b[i])

def merge(a: list[tuple[str,int]], b: list[tuple[str,int]], p: int, q: int, r: int):
    i = p
    k = p
    j = q

    while i < q and j < r:
        if a[i][0] >= a[j][0]:
            b[k] = a[i]
            i += 1
        else:
            a[j][1] += (q - i)
            b[k] = a[j]
            j += 1
        k += 1

    while i < q:
        b[k] = a[i]
        k += 1
        i += 1

    while j < r:
        b[k] = a[j]
        k += 1
        j += 1

    a[p:r] = b[p:r]

def merge_sort(T: list[tuple[str,int]], b: list[tuple[str,int]], p: int, r: int):
    if r - p <= 1:
        return

    q = (r + p) // 2
    merge_sort(T, b, p, q)
    merge_sort(T, b, q, r)

    merge(T, b, p, q, r)


def solution(T: list[str]):
    n = len(T)
    t = [[T[i], 0] for i in range(n)]
    h = [["", 0] for i in range(n)]
    merge_sort(t, h, 0, n)

    top = -1
    for item in t:
        top = max(top, item[1])
    return top


if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))


    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))
