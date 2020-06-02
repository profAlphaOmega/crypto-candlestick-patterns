import numpy as np


def bullish_engulfing(candles):
    data = dict()
    data.update({
        'indicies': np.where(
                    (candles['spin'][:-1])  # current is bull
                    &
                    (~candles['spin'][1:])  # previous was bear
                    &
                    (candles['body_high'][:-1] > candles['body_high'][1:])  # high body
                    &
                    (candles['body_low'][:-1] <= candles['body_low'][1:])  # low body
                )
    })
    return data


def bearish_engulfing(candles):
    data = dict()
    data.update({
        'indicies': np.where(
                    (~candles['spin'][:-1])  # current is bear
                    &
                    (candles['spin'][1:])  # previous was bull
                    &
                    (candles['body_high'][:-1] >= candles['body_high'][1:])  # high body
                    &
                    (candles['body_low'][:-1] < candles['body_low'][1:])  # low body
                )
    })
    return data


def doji(ohlcv):
    data = dict()
    data.update({
        'indicies': np.where(ohlcv['open'] == ohlcv['close'])
    })
    return data


def hammer(candles):
    # long lower shadow
    # small body
    # real body towards the top half
    data = dict()
    data.update({
        'indicies': np.where(
            (candles['upper_shadow_pct'] < 0.05)
            &
            (candles['lower_shadow_pct'] > 0.5)
        )
    })
    return data


def gravestone_doji(candles):
    data = dict()
    data.update({
        'indicies': np.where(
            (candles['low'] == candles['open']) & (candles['open'] == candles['close'])
        )
    })
    return data


def dragonfly_doji(candles):
    data = dict()
    data.update({
        'indicies': np.where(
            (candles['high'] == candles['open']) & (candles['open'] == candles['close'])
        )
    })
    return data


def bullish_piercing(candles):
    data = dict()
    data.update({
        'indicies': np.where(
            (~candles['spin'][1:])  # previous was bear
            &
            (candles['spin'][:-1])  # current is bull
            &
            (candles['open'][1:] < candles['close'][:-1])
            &
            (candles['close'][1:] > candles['body_mdpt'][:-1])
        )
    })
    return data


def shooting_star(candles):
    data = dict()
    data.update({
        'indicies': np.where(
            (candles['upper_shadow_pct'] > 0.5)
            &
            (candles['lower_shadow_pct'] < 0.05)
        )
    })
    return data

