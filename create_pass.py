#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import sys
import getpass
import base64
import win32clipboard
import win32con
import platform

def setText(aString):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)
    win32clipboard.CloseClipboard()

if len(sys.argv) == 2:
    if sys.argv[1] == "first":
        FirstKey = raw_input('please input first key: ')
        SecondKey = raw_input('please input second key: ')
    if sys.argv[1] == "login":
        FirstKey = getpass.getpass('please input first key: ')
        SecondKey = getpass.getpass('please input second key: ')
else:
    sys.exit()

lpos = len(FirstKey + SecondKey) % 9
dpos = len(FirstKey + SecondKey) % 7
spos = len(FirstKey + SecondKey) % 28
epos = spos + 12
ans = hashlib.md5()
ans.update(FirstKey)
ans.update(SecondKey)
data = ans.hexdigest()
ans = hashlib.sha1()
ans.update(FirstKey)
ans.update(SecondKey)
data = ans.hexdigest()
data = data[spos:epos]
data = base64.b64encode(data)
data = data.replace(data[lpos], chr(95), 1)
data = data.replace(data[dpos], chr(46), 1)

sysstr = platform.system()
if(sysstr =="Windows"):
    setText(data)
    print u"已存至剪切板"
elif(sysstr == "Linux"):
    print data