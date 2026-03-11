# Given a sorted array of len n containing pipe lengths. Find the size of the largest subset,
# in which every any three pipes can make a triangle
#
# Example: [5,6,10,15,27,34] -> 3
# [3,4,5,6] -> 4

def triangle_pipes(t: list[int])->int:
    n = len(t)
    if n < 3:
        return 0

    longest = 0
    s, e = 0, 2
    while e < n:
        if (t[s] + t[s + 1]) > t[e]:
            e += 1
            longest = max(longest, e - s)
        else:
            s += 1
            e = max(e, s+2)

    return longest

print(triangle_pipes([1,2,3]))
print(triangle_pipes([3,4,5,6]))
print(triangle_pipes([5,6,10,15,27,34]))
