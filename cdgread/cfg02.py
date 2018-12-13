#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'

num_lines = sum(1 for line in open('vlanconfig.cfg'))
print(configlist)
print(num_lines)



## Always close your file
configfile.close()