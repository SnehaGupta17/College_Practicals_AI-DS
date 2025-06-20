# Client
import socket 
import threading  

def receive_messages(client_socket):     
    while True:         
        try:             
            message = client_socket.recv(1024).decode()             
            if message:                 
                print(f"Server: {message}")         
        except Exception as e:             
            print("Connection closed.")             
            break  
        
def start_client(server_ip, server_port=12345):     
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
    client_socket.connect((server_ip, server_port))      
    threading.Thread(target=receive_messages, args=(client_socket,)).start()      
    while True:         
        message = input("You: ")         
        if message == 'exit':             
            client_socket.sendall(b'exit')             
            break         
        elif message.startswith('sendfile:'):             
            filename = message.split(':')[1]             
            client_socket.sendall(f'FILE:{filename}'.encode())         
        else:             
            client_socket.sendall(message.encode())      
            
    client_socket.close()  

if __name__ == "__main__":     # Replace 'localhost' with the server's IP address if not running locally     
    start_client('localhost')