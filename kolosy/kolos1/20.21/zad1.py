from random import random


def partition(T: list[int], l: int, r: int, pivotIndex: int):
    pivot = T[pivotIndex]
    T[pivotIndex], T[r] = T[r], T[pivotIndex]
    p = l
    for i in range(l, r-1):
        if T[i] < pivot:
            T[p], T[i] = T[i], T[p]
            p += 1

    T[r], T[p] = T[p], T[r]
    return p

def quickselect(T: list[int], l: int, r: int, k: int):
    if l == r:
        return T[l]
    pivotIndex = l + int(random() * (r - l + 1))
    pivotIndex = partition(T, l, r, pivotIndex)
    if k == pivotIndex:
        return T[k]
    elif k < pivotIndex:
        return quickselect(T, l, pivotIndex-1, k)
    else:
        return quickselect(T, pivotIndex + 1, r, k)

def print_tab(T: list[list[int]]):
    for row in T:
        print(row)
    print()

def Median(T: list[list[int]]):
    n = len(T)
    total_el = n*n
    helper = [0] * total_el
    i = 0
    for row in T:
        for x in row:
            helper[i] = x
            i += 1

    print(helper)
    quickselect(helper, 0, n*n-1, (total_el-n)//2)
    quickselect(helper, (total_el-n)//2, n*n-1, (total_el-n)//2+n)
    print(helper)

    l = 0
    mid = (total_el-n)//2
    r = mid + n

    for y in range(n):
        for x in range(n):
            if x == y:
                T[y][x] = helper[mid]
                mid += 1
            elif x < y:
                T[y][x] = helper[l]
                l += 1
            else:
                T[y][x] = helper[r]
                r += 1

T = [
   [int(random() * 10) for _ in range(5)] for _ in range(5)
]

print_tab(T)
Median(T)
print_tab(T)