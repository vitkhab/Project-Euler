#!/usr/bin/env python
from time import time


day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def find_solution():
    count = 0
    weekday = 0
    day = 1
    month = 0
    year = 1900
    while year < 1901:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            dim = days_in_month_leap
        else:
            dim = days_in_month
        if weekday == 6:
            weekday = 0
        else:
            weekday += 1
        if day == dim[month]:
            day = 1
            if month == 11:
                month = 0
                year += 1
            else:
                month += 1
        else:
            day += 1
    while year < 2001:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            dim = days_in_month_leap
        else:
            dim = days_in_month
        if weekday == 6:
            weekday = 0
        else:
            weekday += 1
        if day == dim[month]:
            day = 1
            if month == 11:
                month = 0
                year += 1
            else:
                month += 1
        else:
            day += 1
        if day == 1 and weekday == 6:
            count += 1
    return count


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()