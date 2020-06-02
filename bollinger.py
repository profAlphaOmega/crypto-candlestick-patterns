''' TODO 
- put all arrays in a dict: bollinger
- Turn into function with necessary inputs
    lookbacks for scale analysis scanning
- return statment
- general code cleanup
'''
import numpy as np


def calculate(ohlcv):
    avg_bandwidth = np.array([])
    stdev = np.array([])
    stdev_lookback = 20
    sma = []
    sma_lookback = 20
    bandwidth_lookback = 5

    data = dict()

    # Stdev and simple moving average arrays
    for i, e in enumerate(ohlcv['close']):
        stdev = np.append(stdev, np.std(ohlcv['close'][i:i+stdev_lookback]))
        if len(ohlcv['close'][i:i+sma_lookback]) < sma_lookback:
            sma = np.append(sma, 0)
            continue
        sma = np.append(sma, np.average(ohlcv['close'][i:i+sma_lookback]))

    # high/lowbands
    highband = sma + (2 * stdev)
    lowband = sma - (2 * stdev)

    # high/lowcrosses
    highcross = np.where(ohlcv['close'] > highband)
    lowcross = np.where(ohlcv['close'] < lowband)

    # bb band width and average bandwidth
    bandwidth = highband - lowband
    # bandwidth = 100 * (bandwidth/sma)
    for i, elm in enumerate(bandwidth):
        avg_bandwidth = np.append(avg_bandwidth, np.average(bandwidth[i:i+bandwidth_lookback]))

    # percentb
    percentb = (ohlcv['close'] - lowband) / (highband - lowband)

    data.update(
        highband=highband,
        lowband=lowband,
        highcross=highcross,
        lowcross=lowcross,
        percentb=percentb,
        avg_bandwidth=avg_bandwidth,
        stdev=stdev,
        stdev_lookback=stdev_lookback,
        sma=sma,
        sma_lookback=sma_lookback,
        bandwidth_lookback=bandwidth_lookback,
    )

    return data

