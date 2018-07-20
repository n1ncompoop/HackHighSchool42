#!/usr/bin/env python3

import sys

strr = sys.argv[1]
s = True

lenn = ""
for i in strr:
    if (s and i.isalpha()):
        lenn += ((i.upper()))
        s = False
    elif (not s and i.isalpha()):
        lenn += ((i.lower()))
        s = True
    else:
        lenn += i
print (lenn)

vowl = "AEIOU"
lennn = ""

for i in lenn:
    if (i in vowl):
        lennn += "*"
    else:
        lennn += i
print (lennn)

cn1 = 0
cn2 = 0

for i in lennn:
    if i == "(":
        cn1 += 1
    elif i == ")":
        cn2 += 1
if cn1 == cn2:
    print ("Balanced? True")
else:
    print ("Balanced? False")

