#!/usr/bin/env python3

def print_format_table():
    for style in range(8):
        for fg in range(30,38): 
            s1 = ""
            for bg in range(40,48):
                format = ";".join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()

def print_colorful_text(string, style, foreground, background):
    format = ";".join([str(style), str(foreground), str(background)])
    s1 = '\x1b[%sm %s \x1b[0m' % (format, string)
    print (s1, end='')


rainbow = "RAINBOW"

for i, background in zip(rainbow, range(41, 49)):
    print('\n'),
    for foreground in range (30, 38):
        print_colorful_text(i, 1, foreground, background)
