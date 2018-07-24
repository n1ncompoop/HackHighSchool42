#!/usr/bin/env python3

import sys
import os
from collections import defaultdict

basedir = os.path.dirname(__file__)
reldir = "./names.txt"
full_fp = os.path.join(basedir, reldir)

names_list = defaultdict(list)
print("\n**\n***\nSHARED FIRST NAMES\n***\n**\n")
"""shared_first_name"""
with open(full_fp) as nametxt:
    for line in nametxt:
        (key, val) = line.rstrip('\n').split(",")
        names_list[key].append(val)
for i in names_list:
    if len(names_list[i]) > 2:
        strr = ",".join(names_list[i])
        print("%s (%d): [%s]" % (i, len(names_list[i]), strr))



print("\n**\n***\nSHARED LAST NAMES\n***\n**\n")
"""shared_last_name"""
with open(full_fp) as nametxt:
    for line in nametxt:
        (val, key) = line.rstrip('\n').split(",")
        names_list[key].append(val)
for i in names_list:
    if len(names_list[i]) > 2:
        strr = ",".join(names_list[i])
        print("%s (%d): [%s]" % (i, len(names_list[i]), strr))
