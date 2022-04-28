import datetime

y = 2022
m = 4
da = 31


def last_date(y, m, da):
    try:
        d = datetime.datetime(y, m, da)
        return d
    except:
        return last_date(y, m, da - 1)


print(last_date(y, m, da).strftime("%A"))
