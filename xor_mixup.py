for _ in range(int(input())):
    input()
    from functools import reduce
    import operator
    print(reduce(operator.xor,map(int,input().split())))