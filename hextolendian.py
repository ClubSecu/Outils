#!/usr/bin/python
import struct
import os
import sys
import string

if len(sys.argv) is not 2:
    print "Usage : ", sys.argv[0], " [0x00000000]"
    sys.exit()

result = struct.pack("<I",int(sys.argv[1],16)).encode('string-escape')

print(result)
sys.exit()
