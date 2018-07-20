#!/usr/bin/env python3

inputt = input("string pls\n")
arr = inputt.split()
cnt = 0
for i in arr:
    print("Argv of " + str(cnt) + " is " + i)
    cnt += 1
arr.sort(key = len)
arr.reverse()
for i in arr:
    print(i)
