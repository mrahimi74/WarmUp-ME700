import numpy as np
from main_function import bisection as bisc

def test_avg_x_y():
  x = 10
  y = 20
  assert np.isclose(bisc.Avg(x, y), 15)
  x = 7
  y = 13
  assert np.isclose(bisc.Avg(x, y), 10)
  x = 3
  y = 5
  assert np.isclose(bisc.Avg(x, y), 4)
  x = 18
  y = 24
  assert np.isclose(bisc.Avg(x, y), 21)

def test_sign():
  x = 12
  assert np.isclose(bisc.sign(x), 1)
  x = -4
  assert np.isclose(bisc.sign(x), -1)

def test_abs():
  x = 19
  assert np.isclose(bisc.abs(x), 19)
  x = -241
  assert np.isclose(bisc.abs(x), 241)
  
def test_check():
  x = 12
  y = 17
  assert np.isclose(bisc.check(x,y, True))
  x = 9
  y = 16
  assert np.isclose(bisc.check(x,y,True))

def fn(x):
  return x**2 - 14

def test_opps_sign():
  x = 3
  y = 5
  assert np.isclose(bisc.opps_sign(x, y, True))
