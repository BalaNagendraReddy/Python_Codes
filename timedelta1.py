# Program to add timedelta to timestamp1 until it reaches timestamp2.

from datetime import datetime
from datetime import timedelta

date_format_str = '%d/%m/%Y %H:%M:%S'

# Given timestamps in string
t1 = '28/2/2020 23:12:22'
t2 = '2/3/2020 11:15:22'

# create datetime object from timestamp string
t1_time = datetime.strptime(t1, date_format_str)
t2_time = datetime.strptime(t2, date_format_str)


while t2_time > t1_time:
    # Add 1 minutes to datetime object
    temp_time = t1_time + timedelta(minutes=1)
    # Convert datetime object to string in specific format
    temp_time_str = temp_time.strftime('%d/%m/%Y %H:%M:%S')
    print('Temp Time as string object: ', temp_time_str)
    t1_time = temp_time
