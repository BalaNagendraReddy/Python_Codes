# Program is to calculate the number of days between given date string and the present day.
# Installed Module : pytz
# pip install pytz

import datetime
import pytz


def str_to_datetime(ts):
    fmt = '%Y-%m-%d %H:%M:00'
    return datetime.datetime.strptime(ts, fmt)


def time_now():
    now_utc = datetime.datetime.utcnow()
    local_tz = pytz.timezone('Asia/Kolkata')  # Local timezone which we want to convert the UTC time
    now_utc = pytz.utc.localize(now_utc)  # Add timezone information to UTC time
    x = now_utc.astimezone(local_tz)  # Convert to local time
    timestamp_in_str = x.strftime('%Y-%m-%d %H:%M:00')
    timestamp_in_datetime = datetime.datetime.strptime(timestamp_in_str, '%Y-%m-%d %H:%M:00')
    return timestamp_in_datetime



if __name__ == "__main__":
    rt = '2022-02-28 00:05:00'
    tday = time_now()
    rt_dts = str_to_datetime(rt)
    t1 = tday-rt_dts
    print(t1.days)
