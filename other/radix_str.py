def radix_sort(arr: list[str]) -> None:
    if not arr:
        return

    # Znajdujemy maksymalną długość stringa w liście
    max_len = max(len(s) for s in arr)

    # Sortowanie od ostatniego znaku (LSD) do pierwszego
    for i in range(max_len - 1, -1, -1):
        # Inicjalizujemy kubełki dla tablicy ASCII (0-255).
        # Dla obsługi znaków z całego zakresu Unicode, lepiej użyć słownika
        # (dict) lub metody sortowania opartej na kluczach dla zaoszczędzenia pamięci.
        buckets: list[list[str]] = [[] for _ in range(ord("z") - ord("a") + 2)]

        for s in arr:
            # Jeśli string jest krótszy niż obecna pozycja od lewej,
            # traktujemy "brakujący" znak jako 0 (najwyższy priorytet).
            char_val = ord(s[i]) - ord("a") + 1 if i < len(s) else 0

            # Zabezpieczenie przed znakami spoza standardowego zakresu (opcjonalne)
            if char_val >= 256:
                raise ValueError(f"Znak '{s[i]}' wykracza poza obsługiwany zakres ASCII.")

            buckets[char_val].append(s)

        # Zmiana zawartości oryginalnej listy (modyfikacja in-place)
        idx = 0
        for bucket in buckets:
            for s in bucket:
                arr[idx] = s
                idx += 1


# === Przykład użycia ===
if __name__ == "__main__":
    slowa = ["jablko", "banan", "arbuz", "ananas", "aa", "a", "ab"]
    print("Przed sortowaniem:", slowa)

    radix_sort(slowa)

    print("Po sortowaniu:  ", slowa)