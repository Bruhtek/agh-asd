def radix_sort(T: list[int]):
    n = len(T)
    biggest = max(T)

    helper = [0] * n
    counts = [0] * 10
    exp = 1
    while biggest//exp > 0:
        for i in range(10):
            counts[i] = 0
        for i in range(n):
            counts[(T[i]//exp) % 10] += 1
        for i in range(1,10):
            counts[i] += counts[i-1]

        for i in range(n-1,-1,-1):
            counts[(T[i]//exp) % 10] -= 1
            helper[counts[(T[i]//exp) % 10]] = T[i]
        for i in range(n):
            T[i] = helper[i]
        exp *= 10

nums = [67428094367,43216785094321,45321687954321,53421768954321,4321678954321,432187954312,43216753421,5234168754]
print(nums)
radix_sort(nums)
print(nums)