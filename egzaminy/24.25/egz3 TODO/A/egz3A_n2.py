from egz3Atesty import runtests


def treecut( H, k ):
    s = 0
    i = 1
    n = len(H)
    while i < n and s <= k:
        j = i
        while j > 0 and H[j-1] > H[j]:
            H[j], H[j-1] = H[j-1], H[j]
            s += 1
            j -= 1
        i += 1
    return i if s <= k else i-1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( treecut, all_tests = True )
