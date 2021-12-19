#!/usr/bin/python
#https://codingbee.net/centos/openssl-demo-encrypting-decrypting-files-using-bo$
#Used to generate two keys using two different commands. Needed for key exchange
import os
genPrivateKeyCMD="openssl genpkey -algorithm rsa -out privateKey.pem -pkeyopt rsa_keygen_bits:256"
k=os.popen(genPrivateKeyCMD).readlines()
publicKeyGen="openssl rsa -pubout -in privateKey.pem -out publicKey.pem"
k=os.popen(publicKeyGen).readlines()

