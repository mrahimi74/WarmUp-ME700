import numpy as np
from main_function import bisection as bs

#Example1 - we're given the equation of deflection of a simply supported beam. we want to find a location where the deflection is 0.002 , E = 1000 MPa, I = 25 mm^4, L = 70mm, q = 20 N/mm
def v(x):
  return 20/(24 * 1000 * 25) * (x**4-2*70*x**3+70**3*x) - 0.002

#bs.bisec(0, 1, 1e-10, v)

#Example2 - Natural frequency of a spring-mass system with K = 100 N/m and m = 10 kg

def frq(w):
    return 100 - 10 * w**2

#bs.bisec(0, 8, 1e-10, frq)


#Example3 - The natural frequency of a beam with two ends being fixed, L = 20mm
def freq(w):
    return np.cos(w * 20) * np.cosh(w * 20) - 1

#bs.bisec(0, 8, 1e-10, freq)


#Example4 - finding the resistence from the Ohm's law where V = 24v, I = 3A

def f(R):
  return 24 - 3 * R

#bs.bisec(0, 10, 1e-10, f)

# finding the intersection of two functions, cos(x) and 3x + 1

def g(x):
  return np.cos(x) - (3*x + 1)

#bs.bisec(0, 10, 1e-10, g)
