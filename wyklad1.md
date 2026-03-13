# Sortowania
- **Dane**
  - tablica
  - lista
  - pliki
- **Czas działania**
  - proste O(n^2)
  - szybkie O(nlogn)
- **Stabilność** - Stabilny algorytm nie zmienia względnej pozycji elementów o tym samym kluczu
- **W miejscu** - Algorytm sortuje "w miejscu" (in place) jeżeli używa tylko O(1) dodatkowej pamięci

## Sortowanie przez scalanie (Merge Sort)
- posortuj rekurencyjnie osobno lewą i prawą część tablicy
- scal w posortowaną

```
[5,1,13,15,4,7,9,5]

[5,1,13,15] [4,7,9,5]

[1,5,13,15] [4,5,7,9]

[1,4,5,5,7,9,13,15]
```

**Implementacja** - `merge_sort.py`

Czas działania:
```
T(1) = C
T(n) = T(n/2) + T(n/2) + C*n
```

O(n) = N*logN

## Sortowanie kopcowe (Heap sort)
Kopiec - drzewo binarne, w którym zawartość każdego z węzłów jest większa lub równa zawartości węzłów w jego poddrzewach
```
        29
    17      19
 9   11   13 17
3 2  1
```
```py
def parent(i): return (i-1)//2
def left(i): return i*2 + 1
def right(i): return i*2 + 2

[29, 17, 19, 9, 11, 13, 17, 3, 2, 1]
```

Implementacja - `heap_sort.py`