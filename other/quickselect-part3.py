import random
import sys


def partition(arr: list[int], l: int, r: int, pivot_val: int)->tuple[int,int]:
    subarr = arr[l:r+1]
    lower = [x for x in subarr if x < pivot_val]
    equal = [x for x in subarr if x == pivot_val]
    higher = [x for x in subarr if x > pivot_val]

    lt = l + len(lower)
    gt = l + lt + len(equal) - 1
    arr[l:r+1] = [*lower,*equal,*higher]
    return lt, gt

def median_of_3(a,b,c)->int:
    if (a > b) ^ (a > c):
        return a
    if (b > a) ^ (b > c):
        return b
    return c

def quickselect(arr: list[int], l: int, r: int, k: int)->int:
    if l == r:
        return arr[l]

    a,b,c = arr[l], arr[l + (r-l) // 2], arr[r]
    lt, gt = partition(arr, l, r, median_of_3(a,b,c))

    if k < lt:
        return quickselect(arr, l, lt-1, k)
    elif k > gt:
        return quickselect(arr, gt+1, r, k)
    else:
        return arr[k]


data = [9, 2, 7, 1, 5, 8, 3, 6, 4, 0]
print(quickselect(data, 0, len(data)-1, len(data)//3))
print(quickselect(data, len(data)//3, len(data)-1, len(data)*2//3))
print(data)