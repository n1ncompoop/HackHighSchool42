#!/usr/bin/env python3

arr1 = [False,True,True,None,True,None,None,False,False,None,True,False]
arr2 = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"] 
arr3 = [False,False,None,None,True,True,False,True,None,False,True,None]

a = True
b = True

for i in range(0, len(arr1)):
    a = arr1[i]
    b = arr3[i]
    if arr2[i] == "or":
        print ("%r %s %r => %r" % (arr1[i], arr2[i], arr3[i], a or b))
    elif arr2[i] == "and":
        print ("%r %s %r => %r" % (arr1[i], arr2[i], arr3[i], a and b))
    elif arr2[i] == "==":
        print ("%r %s %r => %r" % (arr1[i], arr2[i], arr3[i], a == b))
    elif arr2[i] == "!=":
        print ("%r %s %r => %r" % (arr1[i], arr2[i], arr3[i], a != b))


