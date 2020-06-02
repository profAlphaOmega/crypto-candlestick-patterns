'''
The OBV is a running total of volume (positive and negative). There are three rules implemented when calculating the OBV. They are:

If today's closing price is higher than yesterday's closing price, then: Current OBV = Previous OBV + today's volume
If today's closing price is lower than yesterday's closing price, then: Current OBV = Previous OBV - today's volume
If today's closing price equals yesterday's closing price, then: Current OBV = Previous OBV

'''
import numpy as np


def calculate(ohlcv):
    '''
    TODO
    You have to reverse the order of the close array to build on the previous_obv
    '''

    obv = np.array([0])  # prepoluate first value
    # might need to put a rounding function for the price for equal obv days
    close_diff = np.round(ohlcv['close'][:-1] - ohlcv['close'][1:])
    # close_diff = np.flipud(close_diff)
    # close_diff = np.insert(close_diff, 0, 0)  # need a starting diff value
    # volume = np.flipud(volume)
    # close_diff = np.append(close_diff, 0)  #
    previous_obv = 0

    # current_obv, previous_obv = np.vectorize(_obv_compare)(close_diff, previous_obv, volume)
    for cd, v in zip(reversed(close_diff), reversed(ohlcv['volume'])):
        if cd > 0:
            current_obv = previous_obv + v
        elif cd < 0:
            current_obv = previous_obv - v
        else:
            current_obv = previous_obv
        previous_obv = current_obv
        obv = np.insert(obv, 0, current_obv)  # don't need to flipud if inserting
        # obv = np.insert(obv, 0, current_obv)  # don't need to flipud if inserting

    return obv


# # vectorize functions
# def _obv_compare(cdiff, previous_obv, volume):
#     if cdiff > 0:
#         current_obv = previous_obv + volume
#     elif cdiff < 0:
#         current_obv = previous_obv - volume
#     else:
#         current_obv = previous_obv
#     previous_obv = current_obv
#     return current_obv, previous_obv
