from collections import deque
from kolutesty import runtests


def projects(n: int, L: list[tuple[int, int]]):
    q = deque([])
    # dep[i] = [k] means that i depends on k being done
    dep = [[] for _ in range(n)]
    for a,b in L:
        dep[a].append(b)

    dep_left = [len(dep[i]) for i in range(n)]

    # req[k] = [i] means that i depends on k
    req = [[] for _ in range(n)]
    for a,b in L:
        req[b].append(a)

    for i in range(n):
        if dep_left[i] == 0:
            q.append(i)

    q.append(-1) # -1 is a stopper that says that now we are doing the new set
    res = 0
    while len(q) > 1:
        proj = q.popleft()
        if proj == -1:
            res += 1
            q.append(-1)
            continue

        for r in req[proj]:
            dep_left[r] -= 1
            if dep_left[r] == 0:
                q.append(r)

    return res + 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(projects, all_tests=True)
