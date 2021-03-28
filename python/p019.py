# Counting Sundays

from datetime import datetime


def dotw(day, month, year):
    day = datetime(year, month, day)
    return day.weekday()


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays = 0

for y in range(1901, 2000+1):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        for m in range(len(months_leap)):
            if dotw(1, m+1, y) == 6:
                sundays += 1
    else:
        for m in range(len(months)):
            if dotw(1, m+1, y) == 6:
                sundays += 1

print(sundays)
