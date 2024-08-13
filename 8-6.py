from datetime import date
day_now = date.today()
print(day_now)

bthday = date(2006, 1, 27)
td = day_now - bthday
print(td)
