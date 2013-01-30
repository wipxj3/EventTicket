__author__ = 'DEXTER'
import socket
address = "localhost"
port = 5555
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((address, port))
print "< SERVER CONNECTED >"
while True:
    message = 'generate '
    #Extract Method
    #criteria = ['cinema[1-4]', 'day[1-7]', 'time_stamp[1-5]', 'movie[1-6]', 'locul[1-99]']
    #lst = [int(raw_input('Input '+str(criteria[i])+': ')) for i in range(0,5)]
    #request = str(lst[0])+','+ str(lst[1]) +','+ str(lst[2]) +','+ str(lst[3]) +','+ str(lst[4])
    request = init_request()
    print request
    clientSocket.send(message + request)
    raw_input()

    if message[:9] == 'generate ':
        f = open('.//phone//CinemaTicket.png', 'wb')
        while True:
            buf = clientSocket.recv(4096)
            f.write(buf)
            f.close()
            break
        print "> I recieved from server a file! "
        break
    else:
        clientRecieved = clientSocket.recv(4096)
        print "> I recieved from server: \n", clientRecieved
        #Decompose Conditional
        #if (clientRecieved=="bye-bye") or (clientRecieved=="down"):
        if isConnClosed(clientRecieved):
            clientSocket.shutdown(2)
            clientSocket.close()
            break

def init_request(self):
    criteria = ['cinema[1-4]', 'day[1-7]', 'time_stamp[1-5]', 'movie[1-6]', 'locul[1-99]']
    lst = [int(raw_input('Input '+str(criteria[i])+': ')) for i in range(0,5)]
    request = str(lst[0])+','+ str(lst[1]) +','+ str(lst[2]) +','+ str(lst[3]) +','+ str(lst[4])
    return request

def isConnClosed(self,clientRecieved):
    return (clientRecieved=="bye-bye") or (clientRecieved=="down") or (clientRecieved=="close") or (clientRecieved=="Close") or (clientRecieved=="CLOSE")
