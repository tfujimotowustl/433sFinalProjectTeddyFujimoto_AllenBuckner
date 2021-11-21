#!/usr/bin/python
import os
generateCMD="openssl genrsa -aes256 -out privateKey.pem"
k=os.popen(generateCMD).readlines()
publicKeyGen="openssl rsa -in privateKey.pem -pubout > publicKey.pem"
k=os.popen(publicKeyGen).readlines()
