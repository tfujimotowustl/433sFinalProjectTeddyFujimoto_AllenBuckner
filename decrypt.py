#!/usr/bin/python
import sys
import os
file=sys.argv[1]
keyFile=sys.argv[2]
encryptCMD="openssl rsautl -decrypt -inkey "+ keyFile + " -in "+file+"  -out plain.txt"$
k=os.popen(encryptCMD).readlines()
