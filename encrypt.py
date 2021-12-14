#!/usr/bin/python
import sys
import os
message=sys.argv[1] #takes some message
keyFile=sys.argv[2] #takes some key
f=open("message.txt",'w') #writes to a new message file
f.write(message)
f.close()
encryptCMD="openssl rsautl -encrypt -inkey "+keyFile+" -pubin -in message.txt -out cipher.bin$
k=os.popen(encryptCMD).readlines()
rmCmd="rm message.txt"
l=os.popen(encryptCMD).readlines()

