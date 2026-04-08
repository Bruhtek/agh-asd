import random

def partition(arr: list[int], l: int, r: int, pivot_idx: int)->int:
    arr[r], arr[pivot_idx] = arr[pivot_idx], arr[r]
    ref = arr[r]

    stored_idx = l
    for i in range(l, r):
        if arr[i] < ref:
            arr[stored_idx], arr[i] = arr[i], arr[stored_idx]
            stored_idx += 1

    arr[r], arr[stored_idx] = arr[stored_idx], arr[r]
    return stored_idx

def quickselect(arr: list[int], l: int, r: int, k: int)->int:
    if l == r:
        return arr[l]

    pivot_idx = random.randint(l, r)
    pivot_idx = partition(arr,l,r,pivot_idx)

    if pivot_idx == k:
        return arr[k]
    elif k < pivot_idx:
        return quickselect(arr, l, pivot_idx - 1, k)
    else:
        return quickselect(arr, pivot_idx + 1, r, k)


data = [9, 2, 7, 1, 5, 8, 3, 6, 4, 0]
print(quickselect(data, 0, len(data)-1, len(data)//2))
print(data)