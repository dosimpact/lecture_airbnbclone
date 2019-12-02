# *args **kwargs
def plus(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    print(a + b)


plus(1, 2)
plus(1, 2, 3, 4, 5)
plus(1, 2, 3, 4, 5, z1=1, z2=2, z3=3)  # a= 1 이런식으로 주면 모호함(애러)
