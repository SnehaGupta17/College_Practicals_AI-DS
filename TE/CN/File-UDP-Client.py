import socket
import os

SIZE = 1024

def send_file_data(fp, sockfd, addr):
    # Sending the data
    for line in fp:
        print(f"[SENDING] Data: {line.strip()}")
        n = sockfd.sendto(line.encode(), addr)
        if n == -1:
            print("[ERROR] sending data to the server.")
            os._exit(1)

    # Sending the 'END'
    sockfd.sendto(b'END', addr)
    fp.close()

def main():
    # Defining the IP and Port
    ip = "127.0.0.1"
    port = 8080

    # Creating the socket
    try:
        server_sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(f"[ERROR] Socket creation error: {e}")
        os._exit(1)

    server_addr = (ip, port)

    # Reading the text file
    filename = "client.txt"
    try:
        fp = open(filename, "r")
    except FileNotFoundError:
        print("[ERROR] File not found.")
        os._exit(1)

    # Sending the file data to the server
    send_file_data(fp, server_sockfd, server_addr)

    print("[SUCCESS] Data transfer complete.")
    print("[CLOSING] Disconnecting from the server.")

    server_sockfd.close()

if __name__ == "__main__":
    main()
