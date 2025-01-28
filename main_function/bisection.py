from basic_functions import functions as fn

def bisec(a, b, tol, func):
    if func(a) * func(b) > 0:
        raise ValueError("The function at a and b must have different signs")
    else:
        c = fn.Avg(a, b)
        while fn.abs(c - a) > tol or func(c) > tol:
            if fn.sign(func(c)) == fn.sign(func(a)):
                a = c
            else:
                b = c

            c = fn.Avg(a, b)
        return c
