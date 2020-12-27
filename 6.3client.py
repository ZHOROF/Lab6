import socket
import sys
import os

ClientSocket = socket.socket()
host = '10.0.2.16'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#Response = ClientSocket.recv(1024)
#print(Response)

print('Welcome to Calculator')
while True:
    print('1 - Square Root')
    print('2 - Logarithm')
    print('3 - Exponetial')
    print('0 - Exit')
    data = str(input("Please enter your choice: "))

    if data == '1':

        num = input("Enter value here for calculation :")
        ClientSocket.send(num.encode())
        result = ClientSocket.recv(2048)

        print("The answer is : " + str(result.decode('utf-8')))

    elif data == '2':
        root = True
        while root:

            num = input("Enter value here for Square Root calculation :")
            if int(num) > -1:
                root = False
                ClientSocket.send(num.encode())
                result = ClientSocket.recv(2048)
            else:
                print('\n Enter positive number!!')

         print("The answer is : " + str(result.decode('utf-8')))

    elif data == '3':
        num = input("Enter value here for calculation :")
        ClientSocket.send(num.encode())
        result = ClientSocket.recv(2048)
        print("The answer is : " + str(result.decode('utf-8')))

    elif data == '0':

        ClientSocket.close()
        sys.exit()
    else:
        print('Invalid input')



    #data = input('Enter your operation: \n')
    #ClientSocket.send(data.encode())
   # Response = ClientSocket.recv(1024)
   # print(Response.decode('utf-8'))

ClientSocket.close()


