#!/usr/bin/env python3

import random
import os
from datetime import datetime

categories = {1 : "animal", 2 : "plant", 3 : "food"}
chosen = categories[random.randint(1, 3)]
width = os.get_terminal_size().columns - 1
lst = []
time1 = datetime.now()
"""GET INPUT"""
for i in range(1, 11):
    inputt = input("enter " + chosen + " number " + str(i) + "\n")
    lst.append(inputt)

"""FORMATTING & TIME"""
time1 = "Time taken for copletion: " + str(datetime.now() - time1)
lst.append("============================================")
lst.append(time1)

"""PRINT INPUT"""
print('+' + '=' * (width - 2) + '+')

for x in lst:
    lnnn = int(len(x)/2)
    dddd = int((width / 2) + lnnn)
    cccc = dddd - len(x) + (len(x) % 2)
    print('||%*s%*s' % (dddd, x, cccc, '||'))

print('+' + '=' * (width - 2) + '+')
