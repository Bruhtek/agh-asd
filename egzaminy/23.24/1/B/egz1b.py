from egz1btesty import runtests

inf = float("inf")


def kstrong( T, k):
	n = len(T)
	dp = [[-inf] * (k+2) for _ in range(n)]
	dp[0][0] = T[0]
	for j in range(k+1):
		for i in range(1, n):
			x = T[i]
			dp[i][j] = max(dp[i][j], x, dp[i-1][j] + x)
			dp[i][j+1] = max(dp[i][j+1], x, dp[i-1][j], dp[i-1][j] + x)

	best = -inf
	for j in range(k+1):
		for i in range(n):
			best = max(best, dp[i][j])

	return best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
