#!/usr/bin/env python3

import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(num1 / num2)
num4 = num1 % num2
print(str(num1) + " divided by " + str(num2) + " equals " + str(num3) + " remainder " + str(num4))

a = int(4)
b = float(3.33)
c = complex(2+3j)

print ("Variable a contains " + str(a) + " which is of type: " + type(a).__name__)
print ("Variable a contains " + str(b) + " which is of type: " + type(b).__name__)
print ("Variable a contains " + str(c) + " which is of type: " + type(c).__name__)
