import csv
import string
from typing import List


data = '12/10/22_'
time = '1k:00'
# print(len(data))
# print(len(time))

if len(time) == 5 and time[2] == ':':
    print('da1')
    temp = time.replace(':', '')
    if temp.isdigit():
        print('da2')
    else:
        print('net2')            
else:
    print('net')
