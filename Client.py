import socket
#                                                             IPv4                              TCP-Protokoll
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"
port = 44444

client_socket.connect((server_ip, port))

benutzerkennung = input("Gebe den Benutzername:Passwort ein: ")
client_socket.send(benutzerkennung.encode())
#Antwort entgegen
response = client_socket.recv(1024)
print(response.decode())