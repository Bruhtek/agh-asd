import sys
from random import randint, seed

OIOIOI = True


def gt(a: str, b: str)->bool:
    if a == b: return False

    n = len(a)
    m = len(b)

    i, j = 0, 0
    while i < n and j < m and a[i] == b[j]:
        i += 1
        j += 1

    if i == n:
        return False
    elif j == m:
        return True

    return ord(a[i]) > ord(b[i])

def merge(a: list[tuple[str,int]], b: list[tuple[str,int]], startA: int, startB: int, end: int):
    i = startA
    k = startA
    j = startB

    while i < startB and j < end:
        if gt(a[i][0], a[j][0]):
            b[k] = a[i]
            i += 1
        else:
            new_j = (a[j][0], a[j][1] + (startB - i))
            b[k] = new_j
            j += 1
        k += 1

    while i < startB:
        b[k] = a[i]
        k += 1
        i += 1

    while j < end:
        b[k] = a[j]
        k += 1
        j += 1

    for t in range(startA, end):
        a[t] = b[t]

def merge_sort(T: list[tuple[str,int]], b: list[tuple[str,int]], start: int, end: int):
    if end - start <= 1:
        return

    mid = (end + start) // 2
    merge_sort(T, b, start, mid)
    merge_sort(T, b, mid, end)

    merge(T, b, start, mid, end)


def solution(T: list[str]):
    n = len(T)
    tab = [(T[i], 0) for i in range(n)]
    helper = [("", 0) for i in range(n)]
    merge_sort(tab, helper, 0, n)

    top = -1
    for item in tab:
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
