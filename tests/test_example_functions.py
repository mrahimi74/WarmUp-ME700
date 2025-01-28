import numpy as np
from basic_functions import functions as fn

def test_avg_x_y():
  x = 10
  y = 20
  assert np.isclose(fn.Avg(x, y), 15)
  x = 7
  y = 13
  assert np.isclose(fn.Avg(x, y), 10)
  x = 3
  y = 5
  assert np.isclose(fn.Avg(x, y), 4)
  x = 18
  y = 24
  assert np.isclose(fn.Avg(x, y), 21)

def test_sign():
  x = 12
  assert np.isclose(fn.sign(x), 1)
  x = -4
  assert np.isclose(fn.sign(x), -1)

def test_abs():
  x = 19
  assert np.isclose(fn.abs(x), 19)
  x = -241
  assert np.isclose(fn.abs(x), 241)
  
