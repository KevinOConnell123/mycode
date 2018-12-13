#!/usr/bin/env python3

loginfail = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
print('The number of failed log in attempts is ' + str(loginfail))

loginfail = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
print('The number of successful login attempts is ' + str(loginfail))


# Python Program to Get IP Address 

import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)


loginfail = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    tline = keystone_file_lines[i]
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        temp,ipaddress = tline.split('from')
        loginfail += 1 # this is the same as loginfail = loginfail + 1
        print('Failed attempt from:',ipaddress)
print('The number of failed log in attempts is ' + str(loginfail))



