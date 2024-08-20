def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap


is_leap = is_leap_year(2021)

print(is_leap)