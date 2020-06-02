import numpy as np
from datetime import datetime, timedelta


def convert_utc_to_cdt(utc_time, fmt="%Y-%m-%d %H:%M:%S"):
    '''
    :param utc_time: string of utc time 
    :param fmt: what datetime format you want in/out
    :return: string of cdt time
    '''
    dt = datetime.strptime(utc_time, fmt)
    cdt_time = dt - timedelta(hours=5)
    return cdt_time.strftime(fmt)
