'''
## OHLCV ##
time_period_start 	Period starting time (range left inclusive)
time_period_end 	Period ending time (range right exclusive)
time_open 	Time of first trade inside period range
time_close 	Time of last trade inside period range
price_open 	First trade price inside period range
price_high 	Highest traded price inside period range
price_low 	Lowest traded price inside period range
price_close 	Last trade price inside period range
volume_traded 	Cumulative base amount traded inside period range
trades_count 	Amount of trades executed inside period range
## Exchanges ##
url = 'https://rest.coinapi.io/v1/exchanges'
response = requests.get(url, headers=headers)
res = json.loads(response.content.decode('utf8').replace("'", '"'))
## Assets
url = 'https://rest.coinapi.io/v1/assets'
response = requests.get(url, headers=headers)
res = json.loads(response.content.decode('utf8').replace("'", '"'))

'''
import json
import numpy as np
import requests
from datetime import datetime, timedelta
from utils.timezone import convert_utc_to_cdt


class CoinAPI:
    def __init__(self):
        self.API_KEY = 'REDACTED'
        self.headers = {'X-CoinAPI-Key': self.API_KEY}

    def ohlcv(self, exchange, pair, time_start, time_end, period='1DAY'):
        op = np.array([])
        high = np.array([])
        low = np.array([])
        cl = np.array([])
        volume = np.array([])
        trades_count = np.array([])
        time_period_start = np.array([])
        time_period_end = np.array([])
        time_period_start_cdt = np.array([])
        time_period_end_cdt = np.array([])

        # url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1MIN'
        url = f'https://rest.coinapi.io/v1/ohlcv/{exchange}_SPOT_{pair[0]}_{pair[1]}/history?period_id={period}' \
              f'&time_start={time_start}&time_end={time_end}'
        response = requests.get(url, headers=self.headers)
        res = json.loads(response.content.decode('utf8').replace("'", '"'))

        for p in res:
            cl = np.append(cl, p['price_close'])
            op = np.append(op, p['price_open'])
            high = np.append(high, p['price_high'])
            low = np.append(low, p['price_low'])
            volume = np.append(volume, p['volume_traded'])
            trades_count = np.append(trades_count, p['trades_count'])
            time_period_start = np.append(time_period_start, p['time_period_start'])
            time_period_end = np.append(time_period_end, p['time_period_end'])

            # convert from utc to cdt
            d = p['time_period_start'].split('T')
            time_period_start_cdt = np.append(time_period_start_cdt, f"{d[0]} {d[1][:7]}")
            d = p['time_period_end'].split('T')
            time_period_end_cdt = np.append(time_period_end_cdt, f"{d[0]} {d[1][:7]}")

        cl = np.flipud(cl)
        op = np.flipud(op)
        high = np.flipud(high)
        low = np.flipud(low)
        volume = np.flipud(volume)
        trades_count = np.flipud(trades_count)
        time_period_start = np.flipud(time_period_start)
        time_period_start_cdt = np.flipud(np.vectorize(convert_utc_to_cdt)(time_period_start_cdt))
        time_period_end_cdt = np.flipud(np.vectorize(convert_utc_to_cdt)(time_period_end_cdt))
        time_period_end = np.flipud(time_period_end)

        data = dict(
            close=cl,
            open=op,
            high=high,
            low=low,
            volume=volume,
            trades_count=trades_count,
            time_period_start_cdt=time_period_start_cdt,
            time_period_start=time_period_start,
            time_period_end=time_period_end,
            time_period_end_cdt=time_period_end_cdt
        )
        return data

# OHLCV
# Latest
# url = f'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id={API_PERIOD}&limit=10'
# Historical
# GET /v1/ohlcv/{symbol_id}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}





