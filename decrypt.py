#!/usr/bin/python
import sys
import os
file=sys.argv[1]
key=sys.argv[2]
#f=open(keyFile,'r')
#key=f.read()
#f.close()
encryptCMD="openssl enc -aes-256-ctr -d -k "+ key + " -in "+file+"  -out plain.$
k=os.popen(encryptCMD).readlines()
