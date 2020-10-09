def var_parm1(*p):
    return p


def var_param2(**p):
    for x, y in p.items():
        print(x, y)
    print(type(p))


def kwarg_test(one, two, *arg, **kwargs):
    print(one+two+sum(arg))
    print(kwargs)


def main():
    a = var_parm1(1, 2, 3, 4, 5)
    print(a)
    print(type(a))
    var_param2(a=1, b=2, c=5, d=7)
    kwarg_test(3, 4, 5, 6, 7, 8, 9, first=10, second=20, third=30)


main()
