import logging

import class_can_data
can_data = class_can_data.can_data()

import class_spi_to_can
mcp2515 = class_spi_to_can.spi_to_can_brd_exchange(6000)
mcp2515.set_config_mode()
mcp2515.set_baudrate(500)
mcp2515.set_normal_mode()

def change_filter(filter_val):
    global mcp2515
    mcp2515.set_config_mode()
    mcp2515.set_filter(filter_val)
    mcp2515.set_normal_mode()
    
def change_mask(mask_val):
    global mcp2515
    mcp2515.set_config_mode()
    mcp2515.set_mask(mask_val)
    mcp2515.set_normal_mode()

def change_filter_and_mask(filter_val, mask_val):
    global mcp2515
    mcp2515.set_config_mode()
    mcp2515.set_filter(filter_val)
    mcp2515.set_mask(mask_val)
    mcp2515.set_normal_mode()

filter_value_prev = 0
mask_value_prev = 0
check_mode_var_prev = 0xFF

from datetime import datetime

import queue
can_data_queue = queue.Queue()

#UDP_IP = '192.168.43.208'
UDP_IP = '192.168.64.102'
UDP_PORT = 55001

from concurrent import futures
import grpc
import CanService_pb2
import CanService_pb2_grpc
class can_service(CanService_pb2_grpc.CanOperationsServicer):
    def StartMessagesStream(self, request, context):
        while True:
            try:
                can_data_buf = can_data_queue.get(timeout = 1, block=True)
                #print('StartMessagesStream method')
                yield CanService_pb2.CanMessage(Id=can_data_buf[0]['id'], Len=can_data_buf[0]['length'],
                                            Data = bytes(can_data_buf[0]['data']))
            except:
                print('Timeout occured (StartMessagesStream)')
    
    def SayHello(self, request, context):
        print('Entered to SayHello method')
        return CanService_pb2.testMsg_resp(resp='2')

    def SayHelloAgain(self, request, context):
        print('Entered to SayHelloAgain method')
        return CanService_pb2.testMsg_req(req='name')


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2)) #max_workers=2
CanService_pb2_grpc.add_CanOperationsServicer_to_server(can_service(), server)
server.add_insecure_port('[::]:50051')
server.start()
#server.wait_for_termination()

now = datetime.now()
now = now.strftime("%Y_%m_%d_%H:%M:%S")
print('Time: ', now)
file_name = 'uniexpert_%s.log' % (now)
logging.basicConfig(level=logging.INFO,
                    #filename=file_name,
                    filename='uniexpert.log',
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

from time import sleep
count = 0

import threading

def consumer1():
    i=0
    while True:
        print('===============Consumer1 %d' % i)
        buf_temp = can_data_queue.get()
        i += 1
        print('===============data from queue: ', buf_temp)

c1 = threading.Thread(target=consumer1)
#c1.start()

while True:
    rcv_can_data = mcp2515.can_rx_func()
    #if(buf['length'] >= 0 and buf['length'] <= 8):
    if rcv_can_data != None:
        #print('Count: %d, ID %s Len %d Data' %(count, format(buf['id'], 'X'), buf['length']),' '.join(format(x, '02X') for x in buf['data']))
        #logging.info('ID: %s L: %d D: %s' %(format(buf['id'], 'X'), buf['length'],' '.join(format(x, '02X') for x in buf['data'])))
        MESSAGE = b''
        
        if (rcv_can_data[0]['length'] > 0) and (rcv_can_data[0]['length'] <= 8):
            MESSAGE = bytes(str('ID: %s L: %d D: %s' %(format(rcv_can_data[0]['id'], 'X'), rcv_can_data[0]['length'],' '.join(format(x, '02X') for x in rcv_can_data[0]['data']))).encode('utf-8'))
        else:
            MESSAGE = bytes(str('Count: %d ID: %s L: %d' %(count, format(rcv_can_data[0]['id'], 'X'), rcv_can_data[0]['length'])).encode('utf-8'))
        print(MESSAGE)
        can_data_queue.put(rcv_can_data)
        #udp_sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        count += 1
        print('Count = %d'%count)
      