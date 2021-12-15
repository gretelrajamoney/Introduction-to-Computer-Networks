# sources used:
# https://docs.python.org/3/howto/sockets.html
# https://zetcode.com/python/socket/
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/_thread.html
# https://people.cs.umass.edu/~arun/590CC/lectures/Sockets.pdf

# call necessary libraries
import socket
import os

# initializes port for the server
server_port = 5001
# creates the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binds the socket to a public local host
server_socket.bind(('127.0.0.1', server_port))

# creates data variable with socket statement
data = "HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# becomes a server socket with one listener
server_socket.listen(1)
# prints out statement regarding where the port is
print("The server on port %d is listening." % server_port)

while True:
    # waits for incoming request
    # creates TCP connection setup
    connection_socket, address = server_socket.accept()
    # recieves message from the connected socket
    # stored message into a variable
    rec_msg = connection_socket.recv(1024)
    # prints out the recieved message from the socket
    print("Recieved: {}".format(str(rec_msg)))
    # stores socket statement into a message to be sent
    send_msg = data
    # encodes the decoded message prior to sending it
    connection_socket.send(send_msg.encode())
    print("Sending>>>>>>>>>>>>")
    # prints decoded socket statement
    print(data)
    print("<<<<<<<<<<<")
    #closes the TCP socket connection before breaking
    connection_socket.close()
    break 




