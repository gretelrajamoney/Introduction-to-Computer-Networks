# sources used:
# https://docs.python.org/3/howto/sockets.html
# https://zetcode.com/python/socket/
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/_thread.html

# call necessary libraries
import socket

# prints out out GET call and our Host
print("Request: GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1")
print("Host: gaia.cs.umass.edu\r\n\r\n")

# creates the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connects to the web server host on port 80 
    # port 80 is the normal http port
    s.connect(("gaia.cs.umass.edu", 80))
    # sends data to our newly created socket
    s.sendall(b"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")

    print
    while True:
        # prints out the recieved bytes
        data = s.recv(1024)

        # if no data, it breaks
        if not data:
            break
        
        # decodes the encoded string
        print(data.decode())