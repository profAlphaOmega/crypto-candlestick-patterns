import candles
import bollinger
import obv
from coinapi import client
from assets.cryptocurrency import assets
import patterns

'''
Main script that gets data from CoinAPI, and runs through patterns and indicators
'''


data = dict()
coinapi = client.CoinAPI()

for a in assets.CRYPTOCURRENCIES:
    d = dict()
    ohlcv = coinapi.ohlcv(
                            exchange=a['exchange'],
                            pair=a['pair'],
                            period=a['period'],
                            time_start=a['time_start'],
                            time_end=a['time_end']
                          )
    d.update({'ohlcv': ohlcv})
    d.update({'candles': candles.calculate(d['ohlcv'])})
    d.update({'bollinger': bollinger.calculate(d['ohlcv'])})
    d.update({'obv': obv.calculate(d['ohlcv'])})

    # patterns
    p = dict()
    p.update({'doji': patterns.doji(d['ohlcv'])})
    p.update({'bullish_engulfing': patterns.bullish_engulfing(d['candles'])})
    p.update({'bearish_engulfing': patterns.bearish_engulfing(d['candles'])})
    p.update({'gravestone_doji': patterns.gravestone_doji(d['candles'])})
    p.update({'dragonfly_doji': patterns.dragonfly_doji(d['candles'])})
    p.update({'hammer': patterns.hammer(d['candles'])})
    p.update({'shooting_star': patterns.shooting_star(d['candles'])})
    p.update({'bullish_piercing': patterns.bullish_piercing(d['candles'])})

    # store away
    d.update({'patterns': p})

    #  assets and timeframe
    data.update({f'{a["pair"][0]}_{a["pair"][1]}_{a["period"]}': d})
del d, p, ohlcv
return data