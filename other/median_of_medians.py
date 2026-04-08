def insertion_sort(arr: list[int], l: int, r: int):
    for i in range(l+1, r+1):
        val = arr[i]
        j = i-1
        while j >= l and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr


def three_way_partition(arr: list[int], l: int, r: int, pivot_val: int)->tuple[int,int]:
    lt = l
    i = l
    gt = r

    while i <= gt:
        if arr[i] < pivot_val:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot_val:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    return lt, gt


def median_of_medians(arr: list[int], l: int, r: int)->int:
    n = r - l + 1
    if n <= 5:
        insertion_sort(arr, l, r)
        return arr[l + n//2]

    c = 0
    for i in range(l, r + 1, 5):
        grp_l = i
        grp_r = min(i+4, r)

        insertion_sort(arr, grp_l, grp_r)

        median_idx = i + (grp_r - i) // 2
        arr[l + c], arr[median_idx] = arr[median_idx], arr[l+c]
        c += 1

    return median_of_medians(arr, l, l+c-1)

def select(arr, k, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(arr)-1

    if l == r:
        return arr[l]

    pivot = median_of_medians(arr, l, r)
    lt, gt = three_way_partition(arr, l, r, pivot)
    if k < lt:
        return select(arr, k, l, lt-1)
    elif k > gt:
        return select(arr, k, gt+1, r)
    else:
        return arr[k]

data = [9, 2, 7, 1, 5, 8, 3, 6, 4, 0]
print(select(data, len(data)//3))
print(select(data, (len(data)*2)//3, len(data)//3))
print(data)