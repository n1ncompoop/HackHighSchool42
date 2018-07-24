#!/usr/bin/env python3

text = input("Try a palindrome!\n")
lower = text.lower()
clean = ""
for i in lower:
    if i.islower():
        clean += i
#print clean

leng = len(clean) - 1
start = 0
while start < leng:
    if clean[start] == clean[leng]:
        start += 1
        leng -= 1
    else:
        print("Not a palindrome :(")
        break
if start >= leng:
    print("Nice you found a palindrome!")
