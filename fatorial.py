def fatorial(n):
    res = 1
    for i in range(n, 1, -1):
        res = res * i
    return res
