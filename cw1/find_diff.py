# Given an X and a sorted array, find two numbers i and j so that T[i] - T[j] = x

def find_diff(T: list[int], x: int)->tuple[int,int]|None:
    n = len(T)
    if n < 2:
        return None
    i, j = 0,
    while j < n:
        val = T[i] - T[j]
        if x == val:
            return i,j
        if x > val:
            j += 1
        else:
            i += 1

    return None
