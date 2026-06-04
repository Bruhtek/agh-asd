from kol3testy import runtests


# S total = S zost + S wyciete
# jako że S zost mod m = 0, to S total mod m = S wyciete mod m
# dp[r] - minimalna liczba drzew, które trzeba wyciąć aby otrzymać resztę r

def orchard(T, m):
    S = sum(T) % m

    if S == 0:
        return 0

    filtered_T = [x % m for x in T if x % m != 0]

    # dp[r] - minimalna liczba drzew, które trzeba "wziąść" do sumy, aby otrzymać reszę r
    dp = [float('inf')] * m
    dp[0] = 0
    for val in filtered_T:
        new_dp = dp[:]

        for r in range(m):
            if dp[r] != float('inf'):
                new_r = (r + val) % m
                new_dp[new_r] = min(dp[new_r], dp[r] + 1)

        dp = new_dp

    # wycinamy te drzewa, aby zneutralizować początkową sumę
    return dp[S]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
