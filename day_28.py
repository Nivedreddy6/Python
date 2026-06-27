'''import datetime
today = datetime.date.today()
print(today)
import datetime
now=datetime.datetime.now()
print(now.time())

Common format code
------------------
%d---->Day
%m---->Month
%Y----> year
%H----> Hours
%M----> Min
%S---->sec

strftime()
----------
--> This used to format date and time
import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))
''''''''''''''''''
import datetime
d1=datetime.date(2026,1,26)
d2=datetime.date(2026,2,26)
print("diff b/w to months:",d2-d1)
'----------------------------------
import datetime
any=datetime.datetime.now()
print(any.hour)
print(any.minute)
print(any.second)
print(any.microsecond)
'''
