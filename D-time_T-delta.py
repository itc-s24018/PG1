import datetime as dt 
t_delta = dt.timedelta(days=1)
niti = dt.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(niti + t_delta)

