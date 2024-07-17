import sys, os
import numpy as np
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)
from b_psp import misc_functions as misc_FN
from b_psp import load_PSP_mag

def test_calc_Bmag():
  # loading in some BRTN from PSP FIELDS
  start_time, end_time = '2018-11-5', '2018-11-6'
  time, BRTN = load_PSP_mag.load_B(start_time, end_time) 

  # using our calc_Bmag function
  Bmag = misc_FN.calc_Bmag(BRTN)

  # using numpy's norm calculator
  Bmag_np = np.linalg.norm(BRTN, axis=0)

  print(Bmag, Bmag_np)

  # now testing if they are equal (upto some numerical threshold)
  np.testing.assert_array_almost_equal(Bmag, Bmag_np, decimal=2)