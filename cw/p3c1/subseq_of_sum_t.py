import random


def can_be_found(A: list[int], s: int):
    n = len(A)

    dp: list[list[bool]] = [[False] * (s+1) for _ in range(n+1)]


A = [random.randint(1,1000) for _ in range(50)]
print(can_be_found(A, 100))