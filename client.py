# imports necessary python libraries
import socket

# function definition for the client program
def clientprogram():
    # assigns the host variable to local host
    host = "localhost"
    # assigns a port number for the socket
    port = 1212

    # prints out the host and port the client is connected on
    print('connected to the host: ' + host)
    print('connected to the port: ' + str(port))

    # create an INET, STREAMing socket called clientsocket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client socket connection syntax from the website:
    # https://www.journaldev.com/15906/python-socket-programming-server-client
    # connects the client socket to the server using the host and port
    clientsocket.connect((host, port))

    # prints out necessary prompts from example
    print('type /q to quit the program')
    print('pls enter a message to send to the server')
    # takes in user message and stores it
    message = input('>')
    # encodes it and then sends it to the server
    clientsocket.sendall(message.encode())
    # value that terminates the client server connection
    quitmessage = '/q'
    # sets the value of data to zero to start while loop
    data = 0

    # continues the chat as long as the message is not '/q'
    while message != quitmessage and data != quitmessage:
        # encodes it and then sends it to the server
        clientsocket.sendall(message.encode())
        # recieves the data stream of less than or equal to 1024 bytes
        data = clientsocket.recv(1024).decode()

        # if the data recieved is not equal to the quit terminator
        if data != quitmessage:
            # prints out the message from the server
            print(str(data))
            # takes in user message and stores it
            message = input('>')

        # if the data recieved is equal to the quit terminator
        else:
            # closes the created client socket
            clientsocket.close()
            # exit the program
            exit()
    
    # closes the created client socket
    clientsocket.close()


# program main for the clientprogram() function call
if __name__ == '__main__':
    clientprogram()