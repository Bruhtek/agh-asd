# Given possible change values, like [1,5,8] find the lowest amount of coins required to give out specific change
import sys

sys.setrecursionlimit(100000000)

def lowest_amount(denom: list[int], req: int):
    counts = [0] * (req + 1)

    def recur(a: int)->int:
        if a == 0: return 0
        if counts[a] > 0: return counts[a]

        minAmount = 1e12
        for coin in denom:
            if coin <= a:
                minAmount = min(minAmount, recur(a-coin) + 1)

        counts[a] = minAmount
        return counts[a]

    return recur(req)


print(lowest_amount([1,5,8,7,8,9,1000], 21321))