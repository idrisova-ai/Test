from datetime import datetime

birthday = input().split(" ")
bday = int(birthday[0])
bmonth = int(birthday[1])

current_year = input().split(" ")
day = int(current_year[0])
month = int(current_year[1])
year = int(current_year[2])

byear = 0
if bmonth > month:
    byear = year
elif bmonth < month:
    byear = year + 1
elif bmonth == month:
    if bday >= day:
        byear = year
    else:
        byear = year + 1

flag = False
cyear = year
count = 0
if bmonth == int("02") and bday == int("29"):
    while flag is False:
        if cyear % 4 == 0 and (cyear % 100 != 0 or cyear % 400 == 0):
            byear = cyear
            bday = int("28")
            flag = True
        else:
            cyear += 1
            count += 1
else:
    count = 1


def calculate_dates(birthday, current, flag):
    delta1 = datetime(current.year, birthday.month, birthday.day)
    delta2 = datetime(current.year + count, birthday.month, birthday.day)
    if flag:
        return (delta2 - current).days
    else:
        return ((delta1 if delta1 >= current else delta2) - current).days


if flag:
    birthday_date = datetime(byear, bmonth, bday)
    current_date = datetime(year, month, day)
    c = calculate_dates(birthday_date, current_date, flag) + 1
    print(c)
else:
    birthday_date = datetime(byear, bmonth, bday)
    current_date = datetime(year, month, day)
    c = calculate_dates(birthday_date, current_date, flag)
    print(c)
