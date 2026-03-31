from kol1btesty import runtests

def sort_word(wrd: str)->list[int]:
    letters = [0] * 26
    for c in wrd:
        letters[ord(c) - ord("a")] += 1

    return letters

def f(T: list[str]):
    k = len(T)
    vects = [sort_word(w) for w in T] # O(łączna liczba liter)

    for i in range(25, -1, -1):
        max_val = 0
        for tup in vects:
            max_val = max(tup[i], max_val)

        count = [0] * (max_val + 1)
        for tup in vects:
            count[tup[i]] += 1

        for j in range(1, len(count)):
            count[j] += count[j - 1]

        out = [None] * k
        for j in range(k-1, -1, -1):
            tup = vects[j]
            val = tup[i]
            count[val] -= 1
            out[count[val]] = tup

        vects = out

    best = 1
    curr = 1
    prev = vects[0]
    for i in range(1, k):
        val = vects[i]
        if val == prev:
            curr += 1
            continue

        best = max(best, curr)
        prev = val
        curr = 1

    return max(best, curr)


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
