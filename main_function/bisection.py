def Avg(x, y):
    return (x + y) / 2

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def check(a: float, b: float):
    if a >= b:
        raise ValueError(f"Invalid input: {a} is greater than {b}.")
    return True


def opps_sign(a, b, func):
    if func(b) * func(a) < 0:
        return True
    else:
        raise ValueError("f(a) and f(b) must have opposite signs")

def bisec(a, b, tol, func):
    if opps_sign(a, b, func):
        c = Avg(a, b)
        while abs(c - a) > tol or func(c) > tol:
            if sign(func(c)) == sign(func(a)):
                a = c
            else:
                b = c

            c = Avg(a, b)
    return c
