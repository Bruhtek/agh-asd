# Given a sorted array T of len = n, containing different ints of 0...m-1 (where n < m) -
# Find the smallest integer not present in T
#
# For example given [0,1,2,4,5] it should return 3

def find_smallest(T: list[int]):
    n = len(T)

    start = 0
    end = n-1

    while start != end:
        mid = (start + end)//2
        val = T[mid]
        if val > mid:
            end = mid
        else:
            start = mid + 1

    return start


print(find_smallest([0,1,2,3,5,6,7,8]))