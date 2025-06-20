# Server
import socket 
import threading 
import os  

def handle_client(client_socket):     
    while True:         # Receive a message from the client         
        message = client_socket.recv(1024).decode()         
        if message == 'exit':             
            print("Client disconnected.")             
            break         
        elif message.startswith('FILE:'):             
            filename = message.split(':')[1]             
            if os.path.exists(filename):                 
                with open(filename, 'rb') as f:                     
                    client_socket.sendall(f.read())                 
                print(f'Sent file: {filename}')             
            else:                 
                client_socket.sendall(b'File not found.')         
        else:             
            print(f"Client: {message}")             
            response = input("You: ")  # Server can send a response             
            client_socket.sendall(response.encode())      
    client_socket.close()  

def start_server(host='0.0.0.0', port=12345):     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
    server_socket.bind((host, port))     
    server_socket.listen(1)      
    print(f"Server listening on {host}:{port}")      
    while True:         
        client_socket, addr = server_socket.accept()         
        print(f"Connection from {addr}")         
        threading.Thread(target=handle_client, args=(client_socket,)).start()  
        
if __name__ == "__main__":     
    start_server()
