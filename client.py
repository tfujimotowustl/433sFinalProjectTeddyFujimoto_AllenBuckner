import socket
import random
from threading import Thread
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from colorama import init, Fore, Style

#Initialization for Colors
init()


SERVER_HOST = "192.168.4.63" # The IP address of the server
SERVER_PORT = 5002 # The port we're using on our server

# Set up Socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# Connect to Server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

#Starting Message
print("Hello, Welcome to the Chat Server! Begin Chatting when you're ready!")

def listen_for_messages():
    while True:
        encrypted = s.recv(1024)
        
        #Decryption
        try:
            omessage = private_key.decrypt( 
                encrypted,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print(Fore.GREEN + "\n" + "--> " + omessage.decode() + Style.RESET_ALL)
        #Print received message for display
        except ValueError:
            omessage = ""

# Thread for listening for messages
t = Thread(target=listen_for_messages)
t.daemon = True
# Starts the thread
t.start()

while True:
    to_send =  input() # Gets the messag to send
    message = to_send.encode()
    if to_send.lower() == 'q': #allows q for exiting the program
        break

    #Encryption
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    s.send(encrypted)

s.close()