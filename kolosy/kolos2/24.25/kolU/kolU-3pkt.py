from testy import run_tests

# O(n*k)
def kawa(T: list[int], k: int)->int:
    counts = [0] * (k+1)
    res = 0
    for x in T: # O(n)
        counts[x] += 1
        res += sum(counts[x+1:]) # O(k)

    return res

run_tests(kawa)