import numpy as np
import bisection as bs

#Example1 - we're given the equation of deflection of a simply supported beam. we want to find a location where the deflection is 0.002
#E = 1000 MPa, I = 25 mm^4, L = 70mm, q = 20 N/mm
def v(x):
  return 20/(24 * 1000 * 25) * (x**4-2*70*x**3+70**3*x) - 0.002

bs.bisec(0, 1, 1e-10, v)

