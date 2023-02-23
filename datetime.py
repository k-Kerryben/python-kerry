day = input("When is today?")
Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6

import datetime

# If today is Thursday (0 = Mon, 1 = Tue, 2 = Wen ...)
if datetime.today().weekday() == Thursday:
    print("Yes, Today is Thursday")
elif datetime.today().weekday() == Wednesday:
    print("Today is Wednesday")
elif datetime.today().weekday() == Friday:
    print("Today is Friday")
elif datetime.today().weekday() == Saturday:
    print("Today is Saturday")
elif datetime.today().weekday() == Sunday:
    print("Today is Sunday")
elif datetime.today().weekday() == Monday:
    print("TOday is Monday")
elif datetime.today().weekday() == Tuesday:
    print("Today is Tuesday")
else:
    print("Invalid entry")
exit()