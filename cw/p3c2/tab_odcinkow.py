# Tablica odcinkow, T = [(a1,b1), (a2,b2), ... (an,bn)]
# Q = (a,b)
# Czy jestesmy w stanie uzyskac Q jedynie sklejajac odcinki. W ile odcinkow najmniej? Mozna je skleic jezeli koncowa jednego = poczatkowa drugiego

# rekurencja: dp[i] - czy da sie sleic odcinek Q' = [a, i]
# dla kazdego odcinka ai, bi zrob: dp[bi] = dp[ai]

# Modyfikacja: Majac k sklejen, jaki jest najdluzszy odcinek ktory dostaniemy?

"""
dp n x k

inicjalizacja:
    0 by default
    dp[bi][0] = bi-ai

dla kazdego odcinka ai, bi
dp[bi][j] = max(dp[bi][j], bi - ai + dp[ai][k-1] if dp[ai][k-1] > 0 else 0)

bierz maksa potem z tablicy


prostrze rozwiazanie: przeksztalcic na dag (kazdy wierzcholek ma magiczny numerek, ktory jest liczba),
odcinek ai, bi to krawedz z wierzcholka ai do bi
"""