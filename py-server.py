import socket

def Main():
    host = "127.0.0.1"
    port = 5689
    buffer_time = 1024

    print("Starting up server")

    # create the socket
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try to bind the server to socket
    try:
        ser_socket.bind((host,port))
    except socket.error:
        print("Socket unable to be created.")
    
    print("Server Socket created.")

    ser_socket.listen(3)

    print("Waiting for messages")
    while True:
        conn, addr = ser_socket.accept()

        #print connections
        print("Connections from: %s" % addr[0])

        # received and decode the messaged recieved
        data = conn.recv(buffer_time).decode()
        print(data)

    ser_socket.close()

if __name__ == "__main__":
    Main()