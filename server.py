import socket
from threading import Thread

SERVER_HOST = "192.168.4.63" # The IP address of the server
SERVER_PORT = 5002 # The port we're using on our server

client_sockets = set() #Makes a list for all connected Sockets
s = socket.socket() # creates a socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # makes our port port reusable
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5) #listening for connections
print(f"*** Listening {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):

    while True: #listens for messages
        try:
            msg = cs.recv(1024)
        except Exception as e: #handles when a client disconnects
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)

        for client_socket in client_sockets: #goes through sockets to send messages
            client_socket.send(msg)


while True: #listens for connections
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,)) # thread for listening to messages
    t.daemon = True
    t.start()

#Closes sockets

for cs in client_sockets:
    cs.close()

s.close()