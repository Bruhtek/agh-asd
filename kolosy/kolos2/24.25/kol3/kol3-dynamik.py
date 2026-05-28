from kol3testy import runtests

def print_2d(tab: list[list[int]]):
    for row in tab:
        for x in row:
            print(x, end="\t")
        print()


def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])

    dp = [[float('inf') for _ in range(m)] for _ in range(n)]
    dp[n-1][m-1] = 0
    for i in range(m-2, -1, -1):
        zostalo = C[n-1][i]
        if zostalo <= s:
            dp[n-1][i] = 0
        else:
            prev = C[n-1][i+1]
            if zostalo - prev <= s:
                dp[n-1][i] = dp[n-1][i+1] + 1
            else:
                break
    for i in range(n-2, -1, -1):
        zostalo = C[i][m-1]
        if zostalo <= s:
            dp[i][m-1] = 0
        else:
            prev = C[i+1][m-1]
            if zostalo - prev <= s:
                dp[i][m-1] = dp[i+1][m-1] + 1
            else:
                break

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            curr_s = C[i][j]
            down_s = C[i+1][j]
            right_s = C[i][j+1]

            best_val = float('inf')
            if curr_s - down_s <= s:
                best_val = min(best_val, dp[i+1][j] + 1)
            if curr_s - right_s <= s:
                best_val = min(best_val, dp[i][j+1] + 1)
            dp[i][j] = best_val

    return dp[0][0]


runtests(parkiet, all_tests = True)
