import numpy as np
import matplotlib.pyplot as plt
import pytplot, pyspedas

def load_B(tstart, tend):
    '''
    Function to magnetic fields meaured by PSP for a desired time interval.

    Parameters:
    -----------
    tstart: string 'yyyy-mm-dd'
            Start time in the above format.
    tend: string 'yyyy-mm-dd'
            End time in the above format.

    Returns:
    --------
    time_fld: array_like of np.datetime64
                Array containing time epochs.
    BRTN: array_like of shape (3, Ntimes)
            Array containing the BR, BT, BN time-series.
    '''
    # downloading PSP data from FIELDS
    fields_vars = pyspedas.psp.fields(trange=[tstart, tend], varnames=['psp_fld_l2_mag_RTN_4_Sa_per_Cyc'],
                                    datatype='mag_RTN_4_Sa_per_Cyc', level='l2', time_clip=True)
    # extracting time and BR, BT, BN            
    time_fld = pytplot.data_quants['psp_fld_l2_mag_RTN_4_Sa_per_Cyc'].time.data
    B_RTN = pytplot.data_quants['psp_fld_l2_mag_RTN_4_Sa_per_Cyc'].data.T

    return time_fld, B_RTN

if __name__=='__main__':
    # defining a time window
    start_time, end_time = '2018-11-5', '2018-11-6'
    time, BRTN = load_B(start_time, end_time)