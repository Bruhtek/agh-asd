# Podzielić ciąg a1....an na k spójnych podciągów, tak, aby dostać największą możliwą S (gdzie S to minimalna suma wyrazów w danym podciągu)

# Obserwacja: k podziałów = k-1 podziałów do p + (a_p+1, a_n), więc:
# dp[i][k'] = max po j od 1 do i-1 po min(dp[j][k'-1], Sum od j+1 do po elementach)
# Złożoność O(n^2*k), pamięciowo O(nk) ale można zrobić w O(2n) = O(n)