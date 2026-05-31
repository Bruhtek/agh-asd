def run_tests(fun):
    tests = [
        # (T, k, oczekiwany_wynik)
        ([2, 7, 8, 4], 10, 2),  # Test z zadania
        ([1, 2, 3, 4, 5, 6], 6, 0),  # Posortowane rosnąco
        ([5, 4, 3, 2, 1], 5, 10),  # Posortowane malejąco
        ([3, 3, 3, 3, 3], 5, 0),  # Równe elementy
        ([2, 1, 2, 1, 2, 1], 2, 6),  # Przeplatane
        ([5], 10, 0),  # Jeden element
        ([3, 1, 4, 1, 5, 9, 2, 6], 10, 8)  # Losowe wartości
    ]

    passed = 0
    for i, (T, k, expected) in enumerate(tests):
        # Kopiujemy tablicę, na wypadek gdyby funkcja mutowała wejście
        result = fun(T.copy(), k)
        if result == expected:
            print(f"Test {i + 1} zaliczony!")
            passed += 1
        else:
            print(f"Test {i + 1} BŁĄD! Dla wejścia T={T}, k={k} oczekiwano {expected}, otrzymano {result}")

    print(f"\nWynik: {passed}/{len(tests)} testów zaliczonych.")
