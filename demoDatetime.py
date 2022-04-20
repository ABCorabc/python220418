# demoDatetime.py
import time

#print(dir(time))

# print(time.time())
# #time.sleep(10)
# print(time.time())
# print(time.gmtime())
# print(time.localtime())

#날짜와 시간을 다루는 경우
from datetime import *

#print(dir())

d1 = date.today()
print(d1)
d2 = date(2022, 5, 10)
print(d2)
print(d2 - d1)

d3 = datetime.now()
print(d3)
result = str(d3.year) + "/" + str(d3.month) + "/" + str(d3.day)
print(result)