

class MinHeap:
    def parent(self, i): return (i - 1) // 2
    def left(self, i): return i * 2 + 1
    def right(self, i): return i * 2 + 2

    arr: list[tuple[int,int]] = []

    def size(self):
        return len(self.arr)

    def __init__(self, values=None):
        if values is None:
            values = []

        self.arr = values
        if len(values) > 0:
            start = self.parent(len(values)-1)
            for i in range(start, -1, -1):
                self.heapify_down(i)

    def heapify_down(self, i: int): # Up to O(n)
        smallest = i
        l = self.left(i)
        r = self.right(i)
        n = self.size()
        if l < n and self.arr[l][0] < self.arr[i][0]:
            smallest = l
        if r < n and self.arr[r][0] < self.arr[smallest][0]:
            smallest = r

        if smallest != i:
            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
            self.heapify_down(smallest)

    def heapify_up(self, i: int): # Up to O(n)
        if i == 0:
            return

        p = self.parent(i)
        if self.arr[p][0] > self.arr[i][0]:
            self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            self.heapify_up(p)

    def push(self, val: tuple[int,int]):
        self.arr.append(val)
        self.heapify_up(self.size()-1)

    def pop(self)->tuple[int,int]:
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.arr.pop()

        val = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.heapify_down(0)

        return val


def merge_lists(arrs: list[list[int]])->list[int]:
    total = 0
    n = len(arrs)
    for arr in arrs:
        total += len(arr)

    q = MinHeap()

    res = [-1] * total
    idx = [1] * n
    for i in range(n):
        q.push((arrs[i][0], i))

    i = 0
    while q.size() > 0:
        smallest, arr_idx = q.pop()
        res[i] = smallest
        i += 1

        arr = arrs[arr_idx]
        curr_idx = idx[arr_idx]
        if curr_idx < len(arr):
            q.push((arr[curr_idx], arr_idx))
            idx[arr_idx] += 1

    return res

lists = [
    [1,3,5,7,9,11,13],
    [2,3,5,7,11,13,17],
    [0,0,0,0]
]
print(merge_lists(lists))