def genEven(n):
    i = 0
    while i < n:
        yield i * 2
        i += 1


print(list(genEven(100)))


even = genEven(100)
next(even)
next(even)
next(even)
next(even)
