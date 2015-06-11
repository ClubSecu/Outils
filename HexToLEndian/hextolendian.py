#!/usr/bin/python

""" 
    Author : Nomekrax
    Creation : 10/06/15
    Last modification : 11/06/2015
    Informations : Python 2.7.3
"""

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
