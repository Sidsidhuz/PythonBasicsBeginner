#MODULE TIME
# from time import *
# sleep(1)
# print(time())
# # sleep(1)
# print(localtime(time()))
# # sleep(1)
# print(localtime(mktime((1995,5,10,0,0,0,0,0,0))))
# # sleep(1)
# print(asctime())

# MODULE DATETIME
# from datetime import *
# print(date(2025,6,16))
# d = date.today()
# print(d.weekday())
# print(d.isoweekday())
# print(datetime.now())
# Date = datetime.now()
# print(Date.strftime("%A %D"))
# date1 = date.today()
# date2 = timedelta(days = 5)
# print(date1 + date2)
# print(date1 - date2)

#MODULE CALENDAR
# from calendar import *
# print(calendar(2003))
# print(isleap(2002))
# print(leapdays(2000,2020))
# print(monthrange(2000,12))
# print(month(2025,6,1,1)) #
# print(weekday(2025,12,31))

from random import *
# l = [1,2,3,4,5]
# print(uniform(1,10))
# greet = ['hai','hello','hola','damn']
# print(f"{choice(greet)} SiD")
# ls = (list(range(1,10)))
# shuffle(ls)
# print(ls)
lis = [1,1,2,3,2,1,2,3,3,4,5,6,5,6,6,6,7,8,9]
print(sample(lis,19))
print(randrange(0,19))
l = ['gopi','pigo','pi','go']
print(choices(l,k = 2))
