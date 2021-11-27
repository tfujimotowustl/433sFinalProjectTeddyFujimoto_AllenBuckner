#!/usr/bin/python
import sys
import os
message=sys.argv[1]
keyFile=sys.argv[2]
f=open("message.txt",'w')
f.write(message)
f.close()
encryptCMD="openssl rsautl -encrypt -inkey "+keyFile+" -pubin -in message.txt -$
k=os.popen(encryptCMD).readlines()
rmCmd="rm message.txt"
l=os.popen(encryptCMD).readlines()

