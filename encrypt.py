#!/usr/bin/python
import sys
import os
message=sys.argv[1]
key=sys.argv[2]
f=open("message.bin",'w')
f.write(message)
f.close()
#f=open(keyFile,'r')
#unfilteredkey=f.read()
#f.close()
#key=unfilteredkey.split('\n')[1:-2]
#key='\n'.join(key)
encryptCMD="openssl enc -aes-256-ctr -e -k "+ key + " -in message.bin -out encr$
k=os.popen(encryptCMD).readlines()
