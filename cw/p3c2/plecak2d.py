# Mamy przedmioty, ktore maja trzy parametry: wysokosc, waga, cena
# Plecak ma ograniczenia wysokosciowe oraz wagowe, szukamy najwiekszej wartosci plecakow

"""
Idea: dp[h][w] - maks wartosc plecaka z ograniczeniem h i w

dp[h][w] = max(po kazdym przedmiocie h1, w1, p1: dp[h-h1][w-w1] + p1, dp[h][w])
no i szukamy najwiekszej wartosci w tabelce

"""