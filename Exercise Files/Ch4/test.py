import calendar
from datetime import date
import datetime
from datetime import datetime
from datetime import timedelta

# today=date.today()
# bday=date(today.year,6,30)
# diff=(bday-today).days
# if diff>0:
#   print("Birthday in %d days" % diff)
# else:
#   print("Birthday in %d days" % (diff+365))

# cal = calendar.TextCalendar(calendar.SUNDAY)
# for m in range(1,13):
#     print(cal.formatmonth(2020, m, 0, 0))

# datetime.date()

# today=date.today()
# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print("Tomorrow will be "+days[(today.weekday()+1)%7])

# now=datetime.now()
# print(now.strftime("%d-%b-%Y %H:%M:%S"))

today=date.today()
# Option A:
tomorrow=today+timedelta(days=1)
# Option B:
tomorrow=date(today.year,today.month,today.day+1)