


def bisec(a, b, tol, func):
    if func(a) * func(b) > 0:
        raise ValueError("The function at a and b must have different signs")
    else:
        c = Avg(a, b)
        while abs(c - a) > tol or func(c) > tol:
            if sign(func(c)) == sign(func(a)):
                a = c
            else:
                b = c

            c = Avg(a, b)
        return c
