def a(n, limit):
    if n > limit:
        return
    print("n:", n)
    a(n*n, limit)

a(2, 1000)