import socket
import threading
import sys

class Server:
    def __init__(self, gsm):
        gsm = gsm
        HOST = ''
        PORT = 8888
        threadStatus = {'running': True}
        thread = threading.Thread(target=self.listen, kwargs={'HOST': HOST, 'PORT': PORT, 'gsm': gsm, 'status': threadStatus})

        try:
            thread.start()
        except (KeyboardInterrupt, SystemExit, EOFError):
            threadStatus['running'] = False

    def listen(self, **kwargs):
        # Datagram (udp) socket
        try :
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg :
            print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit(1)
         
        # Bind socket to local host and port
        try:
            s.bind((kwargs['HOST'], kwargs['PORT']))
        except socket.error , msg:
            pass

        s.settimeout(1)
             
        #now keep talking with the client
        while kwargs['status']['running']:
            # receive data from client (data, addr)
            try:
                d = s.recvfrom(1024)
                data = d[0]
                addr = d[1]
                 
                print('Receiving', data)
                print(kwargs['gsm'].addToBuffer(data))

                #kwargs['gsm'].addToBuffer(self.data)
            except:
                pass

