# Opis rozwiązania: stworzenie kopca binarnego o długości k+1 (który dla pierwszego elementu obejmuje każdą pozycję, na której może się znajdować) w czasie O(k)
# następnie wyciągnięcie najmniejszego z tych elementów (i ewentualne dołożenie kolejnego) w czasie O(logk) wykonane O(n) razy, co daje O(nlogk)
# Ostateczna złożoność obliczeniowa zależnie od k:
# k O(1): O(n)
# k O(logn): O(nloglogn)
# k O(n): O(nlogn)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    @staticmethod
    def from_list(values: list[int]):
        dummy = Node(0)
        head = dummy
        for value in values:
            dummy.next = Node(value)
            dummy = dummy.next
        return head.next

    def __repr__(self):
        string = ''
        current = self
        while current:
            if string != "":
                string += ','
            string += str(current.value)
            current = current.next
        return string

class Heap:
    def parent(self,i): return (i-1)//2
    def left(self,i): return i * 2 + 1
    def right(self,i): return i * 2 + 2

    heap: list[Node]

    def __init__(self):
        self.heap = []

    def len(self):
        return len(self.heap)

    def insert(self, node: Node):
        self.heap.append(node)
        i = len(self.heap)-1
        while i > 0:
            p = self.parent(i)
            if self.heap[p].value > self.heap[i].value:
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
            else:
                break

    def heapify(self, i: int):
        smallest = i
        l = self.left(i)
        r = self.right(i)
        if l < self.len() and self.heap[l].value < self.heap[i].value:
            smallest = l
        if r < self.len() and self.heap[r].value < self.heap[smallest].value:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def pop(self)->Node:
        if self.len() == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return top


def SortH(p: Node, k: int)->Node:
    heap = Heap()
    head = p
    curr = head

    warden = Node(0)
    tail = warden
    for i in range(0, k+1):
        if curr is None:
            break
        heap.insert(curr)
        curr = curr.next

    print(tail.value)
    while heap.len() > 0:
        smallest = heap.pop() # O(logk)
        tail.next = smallest
        tail = tail.next

        if curr is not None:
            heap.insert(curr) # O(logk)
            curr = curr.next

    tail.next = None
    return warden.next

T = [1,0,3,2,4,6,5]
tab = Node.from_list(T)
print(tab)
tab = SortH(tab, 1)
print(tab)