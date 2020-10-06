import socket
import logging
#UDP_IP = ""
#UDP_PORT = 55001

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

import threading
import sys

channel = grpc.insecure_channel(('%s:%d'%(TCP_IP, 50051)))
stub = CanService_pb2_grpc.CanOperationsStub(channel)

import queue
can_data_queue = queue.Queue()

class grpc_response_stream_rcv(threading.Thread):
    def __init__(self):
        self.count = 1
        self.receive_stream_enable = True
        self.response = stub.StartMessagesStream(empty_pb2.Empty())

    def receive_stream(self):
        try:
            for i in self.response:
                print('Count = %d, Received from server: %X, Len %d, Data = ' % (self.count, i.Id, i.Len), [j for j in i.Data])
                self.count += 1
                can_data_queue.put(i)
        except:
            print('Class grpc_response_stream_rcv EXCEPT')

    def start_receive_stream(self):
        self.producer = threading.Thread(target=self.receive_stream)
        self.producer.start()

    def stop_thread(self):
        self.response.cancel()