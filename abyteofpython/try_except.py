#!/usr/bin/python
#Filename: try_except.py

import sys

try:
    s = raw_input("please input")
except EOFError:
    print '\n why did you do an EOF on me?'
    sys.exit()
except:
    print '\nSome error/exception occurred'
else:
    print 'else'

print 'Done'