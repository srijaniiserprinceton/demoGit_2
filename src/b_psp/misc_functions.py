import numpy as np

def calc_Bmag(BRTN):
  '''
  Calculates the strength of magnetic field vector.

  Parameters:
  -----------
  BRTN: array_like of floats. Shape (3, Ntimes)
        Array containing the BR, BT, BN time-series.

  Returns:
  --------
  Bmag: array_like of floats. Shape (Ntimes,)
        Array of magnetic field strength.
  '''
  BR, BT, BN = BRTN
  Bmag = np.sqrt(BR**2 +  BN**2 + BT**2) 
  return Bmag