import logging

import class_can_data
can_data = class_can_data.can_data()

import class_spi_to_can
mcp2515 = class_spi_to_can.spi_to_can_brd_exchange(2000)
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

import socket

UDP_IP = "192.168.64.102" #input('Enter IP: ')
UDP_PORT = 55001

buf = datetime.now()
MESSAGE = bytes(str(buf).encode('utf-8'))

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

#MESSAGE = bytes(str('Hello! Count = %d'%count).encode('utf-8'))
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

now = datetime.now()
now = now.strftime("%Y_%m_%d_%H:%M:%S")
print('Time: ', now)
file_name = 'uniexpert_%s.log' % (now)
logging.basicConfig(level=logging.INFO,
                    #filename=file_name,
                    filename='uniexpert.log',
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

from time import sleep
while True:
    sleep(0.01)
    #print("HHH %f"%(time.clock()))
    #logging.info('hello!')
    rcv_can_data = mcp2515.can_rx_func()
    buf = can_data.random_data()
    if(buf['length'] > 0 and buf['length'] <= 8):
        
        print('ID %s Len %d Data' %(format(buf['id'], 'X'), buf['length']),' '.join(format(x, '02X') for x in buf['data']))
        logging.info('ID %s Len %d Data %s' %(format(buf['id'], 'X'), buf['length'],' '.join(format(x, '02X') for x in buf['data'])))
        MESSAGE = bytes(str('ID %s Len %d Data %s' %(format(buf['id'], 'X'), buf['length'],' '.join(format(x, '02X') for x in buf['data']))).encode('utf-8'))
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    else:
        print('ID %s Len %d' %(format(buf['id'], 'X'), buf['length']))
        logging.info('ID %s Len %d' %(format(buf['id'], 'X'), buf['length']))
        MESSAGE = bytes(str('ID %s Len %d' %(format(buf['id'], 'X'), buf['length'])).encode('utf-8'))
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    '''if rcv_can_data != None:
        for i in range(len(rcv_can_data)):
            can_data.append_can_buf(hex(rcv_can_data[i]['id']), rcv_can_data[i]['length'], (rcv_can_data[i]['data']))'''
    
    