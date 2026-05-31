from testy import run_tests

class SumTree:
    n: int
    tree: list[int]

    def parent(self, i: int): return i // 2
    def left(self, i: int): return i * 2
    def right(self, i: int): return i * 2 + 1

    def idx_to_pos(self, i: int): return i + self.n;

    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, idx: int, val: int):
        idx = self.idx_to_pos(idx)
        self.tree[idx] += val

        while idx > 1:
            idx = self.parent(idx)
            self.tree[idx] = self.tree[self.left(idx)] + self.tree[self.right(idx)]


    def query(self, l: int, r: int)->int:
        l = self.idx_to_pos(l)
        r = self.idx_to_pos(r) + 1

        res = 0

        while l < r:
            # Prawe dziecko w drzewie => parent zawiera elementy z poza zakresu [l, r]
            if l % 2 == 1:
                res += self.tree[l]
                l += 1

            if r % 2 == 1:
                r -= 1
                res += self.tree[r]

            l = self.parent(l)
            r = self.parent(r)
        return res


def kawa(T: list[int], k: int)->int:
    tree = SumTree(k+1)
    res = 0
    for x in T:
        tree.update(x, 1)
        res += tree.query(x+1, k)

    return res

run_tests(kawa)