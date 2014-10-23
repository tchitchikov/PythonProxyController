__author__ = 'tchitchikov'
#capture the traffic from the browser
from socket import *
import http.client
import urllib

myHost = ''
myPort = 8090

website = 'http://drudgereport.com'
websitePort = '80'

socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.bind((myHost, myPort))
socket_object.listen(10)
request = open('C:/Users/tchitchikov//Desktop/RequestFile.txt', 'wb')

while True:
    connection, address = socket_object.accept()
    print('Server Connected By: ', address)
    while True:
        data = connection.recv(4096)
        request.write(bytes(data))
        x = http.client.HTTPConnection(host=website, port=80)
        x.request(method='GET', url=website, body=request)
        request.close()

        if not data:
            break
    connection.close()