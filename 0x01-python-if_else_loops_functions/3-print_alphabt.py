#!/usr/bin/python3
#for i in "abcdfghijklmnoprstuvwxyz":
    #print(i, end='')
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end='')
