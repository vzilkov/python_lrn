import socket
import logging
UDP_IP = ""
UDP_PORT = 55001

logging.basicConfig(level=logging.INFO,
                    #filename=file_name,
                    filename='uniexpert_PC_udp_rcv.log',
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

TCP_PORT = 55002
TCP_IP = '192.168.102.247'
tcp_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # TCP
#tcp_sock.connect((TCP_IP, TCP_PORT))
cnt = 1

import grpc
'''
import helloworld_pb2
import helloworld_pb2_grpc
stub = helloworld_pb2_grpc.GreeterStub(grpc.insecure_channel(('%s:%d'%(TCP_IP, 50051))))
response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
print("Greeter client received: " + response.message)'''
import CanService_pb2
import CanService_pb2_grpc
from google.protobuf import empty_pb2
channel = grpc.insecure_channel(('%s:%d'%(TCP_IP, 50051)))
stub = CanService_pb2_grpc.CanOperationsStub(channel)
#response = stub.SayHello(empty_pb2.Empty())
#print("Client received: ", response)
#response = stub.SayHelloAgain(empty_pb2.Empty())
#print("Client received: ", response)

'''
while True:
    #tcp_sock.sendall(b"Hello, world")
    #data = tcp_sock.recv(1024)
    #response = stub.SayHello(helloworld_pb2.HelloRequest(name='Vlad'))
    print("Client received: " + response.message)
    #print('Count= %d, Data received TCP port: %s'%(cnt,data))
    cnt+=1
'''
#sock.bind(("", UDP_PORT))
count = 1
#for a in range(20): 
response = stub.StartMessagesStream(empty_pb2.Empty())
for i in response:
    #string_buf = " ".join(["{:02x}".format(x) for x in (i.Data)])
    print('Count = %d, Received from server: %X, Len %d, Data = ' % (count, i.Id, i.Len), [j for j in i.Data])
    count += 1

'''print('Start loop')
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("Count %d, received message: %s, address %s" % (count,data,addr))
    #logging.info('Count = %d, %s'%(count, data))
    count += 1'''