from kol1atesty import runtests

def g(T: list[str]):
    n = len(T)
    for i in range(n):
        normal = T[i]
        rev = normal[::-1]
        if rev < normal:
            T[i] = rev




# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=False )
