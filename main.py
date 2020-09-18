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

import datetime
now = datetime.datetime.now()
now = now.strftime("%Y_%m_%d_%H:%M:%S")
print('Time: ', now)
file_name = 'uniexpert_%s.log' % (now)
logging.basicConfig(level=logging.INFO,
                    #filename=file_name,
                    filename='uniexpert.log'
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

from time import sleep
while True:
    sleep(0.1)
    #print("HHH %f"%(time.clock()))
    logging.info('hello!')
        rcv_can_data = mcp2515.can_rx_func()
    if rcv_can_data != None:
        for i in range(len(rcv_can_data)):
            can_data.append_can_buf(hex(rcv_can_data[i]['id']), rcv_can_data[i]['length'], (rcv_can_data[i]['data']))
    
    