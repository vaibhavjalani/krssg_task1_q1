
import socket

def client_program():
    host = 'localhost'  
    port = 5000 

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    i=0
    while i<4:
        data1 = client_socket.recv(1024).decode()  
        data2 = client_socket.recv(1024).decode()
        data3 = client_socket.recv(1024).decode()
        data = [int(data1), int(data2), int(data3)]
        print()
        print('Received following cards from casino server: ')  
        j=0
        while j<3:
            while data[j]>13 :
                data[j]=data[j]-13
            j+=1
        print(data)
        max1=max(data[0],data[1],data[2])
        print('Sending the max card numbered ' + str(max1) + ' to the server')
        print()
        client_socket.send(str(max1).encode())  
        i+=1

    data1 = client_socket.recv(1024).decode() 
    data2 = client_socket.recv(1024).decode()
    data3 = client_socket.recv(1024).decode()
    data = [int(data1), int(data2), int(data3)]
    print()
    print('The final scores are as follows :')
    print(data)
    print()
    client_socket.close()  


if __name__ == '__main__':
    client_program()
