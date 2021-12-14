#!/usr/bin/python
import sys
import os
file=sys.argv[1] #takes some file
keyFile=sys.argv[2] #takes some key
encryptCMD="openssl rsautl -decrypt -inkey "+ keyFile + " -in "+file+"  -out plain.txt"$
k=os.popen(encryptCMD).readlines()
