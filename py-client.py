import socket

def Main():
    host = "127.0.0.1"
    port = 5689
    buffer_time = 1024

    # set up socket and connect to port
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((host,port))

    message = "hello world"
    
    c_socket.send(message.encode())

    while True:
        data= c_socket.recv(buffer_time).decode()
        print(data)

    c_socket.close()

if __name__ == "__main__":
    Main()
