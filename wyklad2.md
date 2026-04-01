## Quick Sort

### Idea
- Dostajemy tablicę A (len n) 
- znajdujemy element `x` - pivot - idealnie by było, gdyby podzielił tą tablicę na dwie połówki
- Dzielimy tablicę na dwie - elementy `<= x`, i `>= x`
- Sortujemy je rekurencyjnie

Implementacja w `quick_sort.py`

Złożoność czasowa:
```js
t(1) = c

t(n) = 2*T(n/2) + O(n) // Pod warunkiem idealnych podziałów! => n*logn
t(n) = T(n-1) + O(n) // Pesymistyczne podziały => n^2 I JESZCZE WYJEBIE STACK
t(n) = 2*T((n-1))/2 + O(n) // Co drugi podział zły, a co drugi idealny => też n*logn
```

## Dowód, że  nie da się szybciej niż `nlogn`, jeżeli jedyny dostęp do danych to porównywanie

Sortuję tablicę T z elementami [A, B, C]. Potencjanie poprawnych wyników jest `6` (`3!`)
Wysokość drzewa to pesymistyczna złożoność algorytmu porównań - każde drzewo o wysokości `h` ma najwyżej `2^h` liści, a potrzebujemy min. `n!` liści
`2^h >= n!` <=> `h >= log (n!) >= log ((n/2)^(n/2)) = n/2(logn - 1) => O(nlogn)`

# Sortowania liniowe

## Counting Sort
