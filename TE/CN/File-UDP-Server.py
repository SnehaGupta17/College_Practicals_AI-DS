import socket

SIZE = 1024

def write_file(sockfd, addr):
    filename = "server.txt"
    
    # Creating a file.
    with open(filename, "w") as fp:
        while True:
            buffer, addr = sockfd.recvfrom(SIZE)

            if buffer.decode() == "END":
                break

            print(f"[RECEIVING] Data: {buffer.decode()}")
            fp.write(buffer.decode())

def main():
    # Defining the IP and Port
    ip = "127.0.0.1"
    port = 8080

    # Creating a UDP socket
    server_sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_addr = (ip, port)

    try:
        server_sockfd.bind(server_addr)
    except OSError as e:
        print("[ERROR] bind error")
        exit(1)

    print("[STARTING] UDP File Server started.")
    write_file(server_sockfd, None)

    print("[SUCCESS] Data transfer complete.")
    print("[CLOSING] Closing the server.")

    server_sockfd.close()

if __name__ == "__main__":
    main()

