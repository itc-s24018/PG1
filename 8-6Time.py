from datetime import datetime as dt
now = dt.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(dt(2019,  5, 1, hour=15, minute=15, second=15, microsecond=0))

# 第二引数の時刻(文字)を一時的に左の数字に入れ替える -strptime-
# -strptime- 'str'文字列を'ptime'時間にするメソッド
print(dt.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M"))

