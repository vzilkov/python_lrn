import socket
import logging
UDP_IP = ""
UDP_PORT = 55001

'''logging.basicConfig(level=logging.INFO,
                    #filename=file_name,
                    filename='uniexpert_PC_udp_rcv.log',
                    format='%(asctime)s :: %(levelname)s :: %(message)s')'''

TCP_PORT = 55002
TCP_IP = '192.168.102.247'

import grpc
import CanService_pb2
import CanService_pb2_grpc
from google.protobuf import empty_pb2
channel = grpc.insecure_channel(('%s:%d'%(TCP_IP, 50051)))
stub = CanService_pb2_grpc.CanOperationsStub(channel)

class grpc_response_stream_rcv():
    def __init__(self):
        self.count = count = 1
        self.response = stub.StartMessagesStream(empty_pb2.Empty())

    def receive(self):
        for i in self.response:
            #string_buf = " ".join(["{:02x}".format(x) for x in (i.Data)])
            print('Count = %d, Received from server: %X, Len %d, Data = ' % (self.count, i.Id, i.Len), [j for j in i.Data])
            self.count += 1

class_grpc = grpc_response_stream_rcv()
class_grpc.receive()

'''
response = stub.StartMessagesStream(empty_pb2.Empty())
        for i in response:
            #string_buf = " ".join(["{:02x}".format(x) for x in (i.Data)])
            print('Count = %d, Received from server: %X, Len %d, Data = ' % (count, i.Id, i.Len), [j for j in i.Data])
            count += 1
'''
