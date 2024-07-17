import numpy as np

def calc_Bmag(BRTN):
  BR, BT, BN = BRTN
  Bmag = np.sqrt(BR**2 +  BN**2 + BT**2) 
  return Bmag