def cumlative_sum(n):
    # base case
    if n == 0:
        return 0
    else:
        return n + cumlative_sum(n-1)

print(cumlative_sum(10))