from egz2Btesty import runtests
from math import inf as INF

def bitgame(T):
    stack = []
    for x in T:
        if len(stack) > 0 and stack[-1] <= x:
            while len(stack) > 0 and stack[-1] <= x:
                stack.pop()
        else:
            stack.append(x)

    return len(stack)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( bitgame, all_tests = True )
