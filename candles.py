import numpy as np

'''
Take OHLC and volume data and run calculate common candlestick attributes to detect patterns easier
'''

def calculate(ohlcv):
    # Primitive
    c = dict(ohlcv)
    # derived I
    c.update({'body': abs(ohlcv['open'] - ohlcv['close'])})
    c.update({'wick': ohlcv['high'] - ohlcv['low']})
    c.update({'spin': ohlcv['close'] > ohlcv['open']})
    c.update({'body_pct': c['body'] / c['wick']})
    body_high, body_low = np.vectorize(_highlow)(op=ohlcv['open'], cl=ohlcv['close'])
    c.update({'body_high': body_high, 'body_low': body_low})
    c.update({'lower_shadow': c['body_low']-ohlcv['low']})
    c.update({'lower_shadow_pct': c['lower_shadow']/c['wick']})
    c.update({'upper_shadow': ohlcv['high'] - c['body_high']})
    c.update({'upper_shadow_pct': c['upper_shadow']/c['wick']})
    c.update({'body_mdpt': (c['body']/2) + c['body_low']})
    c.update({'body_mdpttowick': (c['body_mdpt'] - ohlcv['low']) / c['wick']})
    c.update({'wick_mdpt': ((ohlcv['high']-ohlcv['low'])/2) + ohlcv['low']})
    return c


# vectorize functions
def _highlow(op, cl):
    return (op, cl) if op > cl else (cl, op)
# volume = np.array([20,10,10,60,40])
# close = np.array([12,15,9,7,14])
# open = np.array([10,12,15,9,8])
# high = np.array([14,16,20,10,15])
# low = np.array([9,11,3,3,8])
# # ohlcv = np.column_stack((close,open,high,low))
# ohlcv = dict(close=close,open=open,high=high,low=low)
# c = ohlcv(ohlcv)
# print(c)