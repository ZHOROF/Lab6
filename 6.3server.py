import socket
import sys
import time
import errno
import math
from multiprocessing import Process

#ok_message = 'HTTP/1.0 200 OK\n\n'
#nok_message = 'HTTP/1.0 404 NotFound\n\n'


def process_start(s_sock):

    while True:
        data = s_sock.recv(2048).decode()


	#calculate square root
        if data == '1':
                num = s_sock.recv(2048).decode()
                ans = math.log(float(num))

	#calculate log
        elif data == '2':
                num = s_sock.recv(2048).decode()
                ans = math.sqrt(float(num))

	#calculate exponentiol
        elif data == '3':
                num = s_sock.recv(2048).decode()
                ans = math.exp(float(num))


        elif data == '0':
                print('Thank You..')
                s_sock.close()
                break

        #result = "number %s "% str(ans)
        s_sock.sendall(str(ans).encode())


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
        s.close()
