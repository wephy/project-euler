# Counting Sundays

from datetime import datetime

monthsReg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sundays = 0


def dotw(day, month, year):
    day = datetime(year, month, day)
    return day.weekday()


for y in range(1901, 2000+1):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        for m in range(len(monthsLeap)):
            if dotw(1, m+1, y) == 6:
                sundays += 1
    else:
        for m in range(len(monthsReg)):
            if dotw(1, m+1, y) == 6:
                sundays += 1

print(sundays)
