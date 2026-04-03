import sys
import array


def radix_sort(T: array.array[int]):
    n = len(T)
    biggest = max(T)

    BITS = 8
    BASE = 1 << BITS
    MASK = BASE - 1

    helper = array.array("i", [0] * n)
    counts = array.array("i", [0] * BASE)

    shift = 0

    while biggest >> shift > 0:
        for i in range(BASE):
            counts[i] = 0
        for i in range(n):
            counts[(T[i] >> shift) & MASK] += 1

        if counts[0] == n:
            shift += BITS
            continue

        for i in range(1,BASE):
            counts[i] += counts[i-1]

        for i in range(n-1,-1,-1):
            digit = (T[i] >> shift) & MASK
            counts[digit] -= 1
            helper[counts[digit]] = T[i]

        T[:] = helper
        shift += BITS


def main():
    n = int(sys.stdin.readline())
    arr = array.array("i")
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    radix_sort(arr)
    q = int(sys.stdin.readline())
    for i in range(q):
        query = int(sys.stdin.readline())
        print(arr[n-query])

if __name__ == '__main__':
    main()