# Dojsc od 0,0 do x,y; poruszajac sie wylacznie albo w dol albo w prawo, na niektorych polach sa bomby i nie mozna tam wejsc, na ile sposobów można?
# inicjalizacja: dp[0][b] = 1, dp[a][0] = 1, reszta na zera

# rekurencja od a=1 i b=1:  dp[a][b] = dp[a-1][b] if brak bomby na a-1,b else 0 + dp[a][b-1] if brak bomby na a,b-1 else 0
# (No i obviously nie nadpisuj pola jezeli jest tam bomba)