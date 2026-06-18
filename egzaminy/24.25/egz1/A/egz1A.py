from egz1Atesty import runtests

def battle(P: list[int],K: list[int],R: list[int]):
    n = len(P)
    m = len(K)
    maxlen = max(max(P), max(K)) + 1

    procs = [False for _ in range(maxlen)]
    guns = [-1 for _ in range(maxlen)]

    for p in P:
        procs[p] = True
    for i in range(m):
        idx = K[i]
        zasieg = R[i]
        guns[idx] = zasieg

    # contains maxidx for a given gun (doesn't remember it's idx, just the range)
    stack = []
    count = 0
    for i in range(maxlen):
        # mamy katapulte
        if guns[i] != -1:
            max_idx = i + guns[i]
            stack.append(max_idx)
        elif procs[i]:
            curr_idx = i
            while len(stack) > 0 and stack[-1] < curr_idx:
                stack.pop()
            if len(stack) > 0 and stack[-1] >= curr_idx:
                count += 1
                stack.pop()


    return count

runtests( battle, all_tests=True )