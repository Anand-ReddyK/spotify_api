import datetime
# from datetime import datetime
import time
from dateutil import parser
from dateutil import tz
import pytz

def utc_to_local(utc):
    dt = str(parser.parse(utc[:-5])) 
    # dt_str  = "2021-12-18 04:57:19"
    format  = "%Y-%m-%d %H:%M:%S"

    dt_utc = datetime.datetime.strptime(dt, format)
    dt_utc = dt_utc.replace(tzinfo=pytz.UTC)
    local_zone = tz.tzlocal()
    dt_local = dt_utc.astimezone(local_zone)
    local_time_str = dt_local.strftime(format)

    time = local_time_str.split(' ')[-1]
    final_d = local_time_str.split(' ')[0]

    time_con = datetime.datetime.strptime(time, "%H:%M:%S")
    time_con = time_con.strftime("%I:%M %p")
    local_time = final_d + ' ' + time_con
    
    return local_time


# utc_to_local("2021-12-18T04:57:19.958Z")

# ds = '2021-12-15T13:28:26.985Z' # or any date sting of differing formats.
# date = str(parser.parse(ds[:-5]))
# # date = str(date)
# x = date[11:]

# d = datetime.datetime.strptime(x, "%H:%M:%S")
# d = d.strftime("%I:%M %p")


def utc_con(utc):
    dt = str(parser.parse(utc[:-5])) 
    time = dt.split(' ')
    final_d = dt.split(' ')[0]
    
    time_con = datetime.datetime.strptime(time[-1], "%H:%M:%S")
    time_con = time_con.strftime("%I:%M %p")
    local_time = final_d + ' ' + time_con
    return local_time


def yestr_unix_stam():
    today = datetime.datetime.now()
    yestr = today - datetime.timedelta(days=2)
    yestr_unix = int(yestr.timestamp()) * 1000
    return int(today.timestamp()) * 1000

# UTC_datetime = datetime.datetime.utcnow()
# print(type(UTC_datetime))
# UTC_datetime_timestamp = float(UTC_datetime.strftime("%S"))
# print(UTC_datetime_timestamp)
# local_datetime_converted = datetime.datetime.fromtimestamp(UTC_datetime_timestamp)
# print(local_datetime_converted)

# utc_con("2021-12-18T04:57:19.958Z")

