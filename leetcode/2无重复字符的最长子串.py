from datetime import datetime, date

import pandas as pd


def datetime2timestamp(datetime_v):
    # python3
    # if not isinstance(datetime_v, datetime):
    #     return None
    # return int(time.mktime(datetime_v.timetuple()))

    # python3
    if isinstance(datetime_v, datetime):
        return int(datetime.timestamp(datetime_v))
    elif isinstance(datetime_v, date):
        return int(datetime.timestamp(datetime.combine(datetime_v, datetime.min.time())))
    else:
        return None


start_time = 1599840000
end_time = 1600358400
start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d')
end_time = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d')
date_list = [datetime2timestamp(x) for x in list(pd.date_range(start=start_time, end=end_time, freq='D'))]
print(date_list)
