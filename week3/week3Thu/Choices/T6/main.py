def sum_all(a, b, c=100, *args, **kwargs):
    test = True
    if test:
        print(c)
        print(args[0])
        print(args[1])
        print()
    sum = a + b + c
    for d in args:
        sum += d
    for v in kwargs.values():
        sum += v
    return sum
print(sum_all(100, 200, 300, 500, 600, aa=700, bb=900, cc=1000))