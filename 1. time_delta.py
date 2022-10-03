# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
from datetime import datetime

"""
%a indicates the day in three letter format
%d indicates day in numeric format
%b indicates month in three letter format
%Y indicates year in yyyy format
%H indicates hour in hh format
%M indicates minutes in mm format
%S indicates seconds in ss format
%z indicates the timezone in +/- xxxx format
"""


def time_delta(start_date: str, end_date: str):
    date_time_format = '%a %d %b %Y %H:%M:%S %z'
    start = datetime.strptime(start_date, date_time_format)
    end = datetime.strptime(end_date, date_time_format)
    diff = abs(end - start)
    return diff.days * 24 * 60 * 60 + diff.seconds


if __name__ == "__main__":
    test_cases = int(input())

    for test_cases in range(test_cases):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        print(delta, end='\n')

# date1 = 'Mon 03 Sep 2022 23:34:45 +03:00'
# date2 = 'Tue 04 Sep 2022 23:34:45 +03:00'