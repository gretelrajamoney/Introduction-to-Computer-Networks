# imports necessary python libraries
import socket

# function definition for the server program
def serverprogram():
    # assigns the host variable to local host
    host = "localhost"
    # assigns a port number for the socket
    port = 1212

    # prints out the host and port the server is listening on
    print('server listening on the host: ' + host)
    print('server listening on the port: ' + str(port))

    # the following lines are syntax from the 'creating a socket'
    # section of the website: https://docs.python.org/3/howto/sockets.html

    # create an INET, STREAMing socket called serversocket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binds the serversocket to the localhost and port 1212
    serversocket.bind((host, port))
    # becomes a server socket with 2 connect requests
    serversocket.listen(2)
    # accepts connections from outside
    (connection, address) = serversocket.accept()

    # the following lines are syntax from the 'echo server'
    # section of the website: https://realpython.com/python-sockets/
    with connection:
        # prints out the address of the connection
        print("connection from: " + str(address))
        # prints out necessary prompts from example
        print('type /q to quit the program')
        print('waiting for a message from the client...')
        # recieves the data stream of less than or equal to 1024 bytes
        data = connection.recv(1024).decode()
        # value that terminates the client server connection
        quitmessage = '/q'

        while True:
            # recieves the data stream of less than or equal to 1024 bytes
            data = connection.recv(1024).decode()

            # if no data is recieved the statement breaks
            if not data:
                break

            # if the data recieved is equal to the quit terminator
            elif data == quitmessage:
                break

            # if there is data recieved
            else:
                # prints out the message from the connection
                print(str(data))
                # takes in user input and stores it
                message = input('>')
                # value that terminates the client server connection
                quitmessage = '/q'

                # if the users message is not equal to the quit terminator
                if message != quitmessage:
                    # encodes it and then sends it to the connection
                    connection.sendall(message.encode())
                
                # if the users message is equal to the quit terminator
                else:
                    # encodes it and then sends it to the connection
                    connection.sendall(message.encode())
                    # closes the connection
                    connection.close()
                    # exits the program
                    exit()


    # closes the connection
    connection.close()


# program main for the serverprogram() function call
if __name__ == '__main__':
    serverprogram()