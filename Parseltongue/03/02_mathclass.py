#!/usr/bin/env python3

import sys

arrr = []
argc = len(sys.argv)
for i in range(1, argc):
	arrr.append(int(sys.argv[i]))
arrr.sort()
print (arrr)
minn = arrr[0]
argc -= 1
maxx = arrr[argc - 1]
div = argc / 2

if argc % 2 == 0:
	num1 = arrr[int(div - 1)]
	print (num1)
	num2 = arrr[int(div)]
	print (num2)
	median = (num1 + num2) / 2
else:
	median = arrr[int(div)]

num1 = 0
for i in arrr:
	num1 += i

mean = num1 / argc
rangee = maxx - minn
mode = max(set(arrr), key=arrr.count)/////////////

print ("Min: " + str(minn))
print ("Max: " + str(maxx))
print ("Mean: " + str(mean))
print ("Median: " + str(median))
print ("Mode: " + str(mode))
print ("Range: " + str(rangee))
