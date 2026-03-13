def find_min_max(tab: list[int])->tuple[int,int]:
    n = len(tab)
    sm = tab[n-1]
    bg = tab[n-1]
    for i in range(0, n-1, 2):
        if tab[i] < tab[i + 1]:
            if tab[i] < sm:
                sm = tab[i]
            if tab[i + 1] > bg:
                bg = tab[i+1]
        else:
            if tab[i + 1] < sm:
                sm = tab[i+1]
            if tab[i] > bg:
                bg = tab[i]

    return sm, bg


print(find_min_max([1,2,3,4,5,6,7,8,9,10,11]))