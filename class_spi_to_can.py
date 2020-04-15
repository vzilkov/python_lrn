class spi_to_can_brd_exchange:
    import RPi.GPIO as GPIO
    def __init__(self, max_speed_khz):
        self.GPIO.setmode(self.GPIO.BCM)
        self.nCS_pin = 25
        self.GPIO.setup(self.nCS_pin, self.GPIO.OUT)
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
        
        import spidev
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.mode=0b00
        self.spi.lsbfirst=False
        self.spi.max_speed_hz = max_speed_khz*1000
        
        self.device_reset()

    def cs_high(self):
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
        
    def cs_low(self):
        self.GPIO.output(self.nCS_pin, self.GPIO.LOW)

    def spi_close(self):
        self.spi.close()
        self.cs_high()
        
    def device_reset(self):
        self.cs_low()
        
        #INSTRUCTION_RESET = 0xC0
        self.spi.writebytes([0xC0])

        self.cs_high()
    
    def device_read_data(self, adr):
        self.cs_low()
        
        #INSTRUCTION_READ = 0x03
        self.spi.writebytes([0x03, adr])
        read_byte = self.spi.readbytes(1)
        
        self.cs_high()
        return read_byte[0]
        
    def device_write_byte(self, adr, val):
        self.cs_low()

        #INSTRUCTION_WRITE = 0x02
        #buf = [0x02, adr, val]
        self.spi.writebytes([0x02, adr, val])

        self.cs_high()
    
    def read_rx_buf(self):#do I need it???
        self.cs_low()
        
        INSTRUCTION_READ_RX_BUF = 0x90 #0x90 - adr 0x61, 0x92 - adr 0x66, 0x94 - adr 0x71, 0x96 - adr 0x76
        self.spi.writebytes([INSTRUCTION_READ_RX_BUF])
        read_byte = self.spi.readbytes(1)
        
        self.cs_high()
        return read_byte

    def load_tx_buf(self):#do I need it???
        self.cs_low()
        INSTRUCTION_LOAD_TX_BUF = 0x40
        self.cs_high()
        return 1
    
    def req_to_send(self, buf_num): #not tested
        self.cs_low()
        INSTRUCTION_RTS = 0x80 or 0b001 #buf num = 1,2,4 - 1,2,3 tx buffers
        self.spi.writebytes([INSTRUCTION_RTS])
        self.cs_high()
        return 1
    
    def read_status(self):
        self.cs_low()

        #INSTRUCTION_READ_STATUS = 0xA0
        self.spi.writebytes([0xA0])
        read_bytes = self.spi.readbytes(2)

        self.cs_high()

        if read_bytes[0] == read_bytes[1]:
            return read_bytes[0]
        else:
            return 0xFF #error'''
        return read_bytes

    def read_rx_status(self): #not tested
        self.cs_low()

        #INSTRUCTION_RX_STATUS = 0xB0
        self.spi.writebytes([0xB0])
        read_bytes = self.spi.readbytes(2)

        self.cs_high()

        if read_bytes[0] == read_bytes[1]:
            return read_bytes[0]
        else:
            return 0xFF #error'''

    def bit_modify(self, adr_byte, mask_byte, data_byte):#not tested
        self.cs_low()

        #INSTRUCTION_BIT_MODIFY = 0x05
        buf = [0x05, adr_byte, mask_byte, data_byte]
        self.spi.writebytes(buf)

        self.cs_high()
        
    def write_reg_and_check(self, adr, data):
        self.device_write_byte(adr, data)
        return_data = self.device_read_data(adr)
        if data == return_data:
            return return_data
        else:
            return 0xFF

    def check_errors_rec_tec(self):
        TEC = 0x1C
        REC = 0x1D
        ELFG = 0x2D
        errors_rec_tec = [self.device_read_data(REC), 
                        self.device_read_data(TEC),
                        self.device_read_data(ELFG)]
        return errors_rec_tec

    def set_config_mode(self, bit_rate, filter_num):
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
        while self.device_read_data(CANSTAT[0]) & 0x80 != 0x80:
            read_buf = self.device_read_data([CANCTRL[0]])
            read_buf &= 0x1F
            read_buf |= 0x80
            self.device_write_byte(CANCTRL[0], [read_buf])#set to config mode
        print('Config mode in config mode')
        # 500 kbps, Bit rate = 500 
        # Sample point = 75%
        cnf1 = 0b00000011
        cnf2 = 0b00000000 | 2<<3 | 1
        cnf3 = 1
        self.device_write_byte(0x2A, cnf1)
        self.device_write_byte(0x29, cnf2)
        self.device_write_byte(0x28, cnf3)

        #TXRTSCTRL register
        TXRTSCTRL = 0x0D
        self.device_write_byte(TXRTSCTRL, 0) #I don't use pins for TX req
        #Filter registers
        #check check_btn HERE!!!!
        RXB0CTRL = 0x60
        RXB1CTRL = 0x70
        self.device_write_byte(RXB0CTRL, 0)# rx filters don't use default
        self.device_write_byte(RXB1CTRL, 0)

        RXF0SIDH = 0x00
        RXF0SIDL = 0x01

        RXF1SIDH = 0x04
        RXF1SIDL = 0x05

        RXF2SIDH = 0x08
        RXF2SIDL = 0x09

        RXF3SIDH = 0x10
        RXF3SIDL = 0x11

        RXF4SIDH = 0x14
        RXF4SIDL = 0x15

        RXF5SIDH = 0x18
        RXF5SIDL = 0x19

        self.device_write_byte(RXF0SIDH, 0)
        self.device_write_byte(RXF0SIDL, 0)
        
        RXF0EID8 = 0x02
        RXF0EID0 = 0x03
        self.device_write_byte(RXF0EID8, 0)
        self.device_write_byte(RXF0EID0, 0)

        #Mask registers
        RXM0SIDH = 0x20
        RXM0SIDL = 0x21
        RXM1SIDH = 0x24
        RXM1SIDL = 0x25
        self.device_write_byte(RXM0SIDH, 0)
        self.device_write_byte(RXM0SIDL, 0)
        self.device_write_byte(RXM1SIDH, 0)
        self.device_write_byte(RXM1SIDL, 0)
        print('Config mode in config mode completed')

    def set_listen_only_mode(self, filter_num):
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
        print('Listen only mode')
    
    def set_loopback_mode(self, filter_num):#not tested
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]

        while self.device_read_data(CANSTAT[0]) & 0x80 != 0x80:#to config
            read_buf = self.device_read_data(CANCTRL[0])
            read_buf &= 0x1F
            read_buf |= 0x80
            self.device_write_byte(CANCTRL[0], read_buf)#set to config mode
        print('Config mode in loopback mode')

        while self.device_read_data(CANSTAT[0]) & 0x40 != 0x40:#to loopback
            read_buf = self.device_read_data(CANCTRL[0])
            read_buf &= 0x1F
            read_buf |= 0x40
            self.device_write_byte(CANCTRL[0], read_buf)#set to loopback mode
        print('Loopback mode completed')
        
    def set_normal_mode(self):
        #self.set_config_mode(500,0)
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
        
        while self.device_read_data(CANSTAT[0]) & 0x80 != 0x80:#to config
            read_buf = self.device_read_data(CANCTRL[0])
            read_buf &= 0x1F
            read_buf |= 0x80
            self.device_write_byte(CANCTRL[0], read_buf)#set to config mode
        
        while self.device_read_data(CANSTAT[0]) & 0xE0 != 0x00:#to normal
            read_buf = self.device_read_data(CANCTRL[0]) & 0x1F
            self.device_write_byte(CANCTRL[0], read_buf)#set to normal mode
        print('Normal mode completed')
        
    def __check_free_tx_buf(self):#returns number of first free TX buffer
        TXBCTRL = [0x30,0x40,0x50]
        for buf_num in range(3):
            if (self.device_read_data(TXBCTRL[buf_num]) & (1<<3)) == 0:#TXREQ = 0
                print('Free TX buf num = ', buf_num)
                return buf_num
        return 0xFF

    def can_tx_func(self, ID, lenght, *tx_data):#haven't wrote yet
        buf_num = self.__check_free_tx_buf()
        
        TXBCTRL = [0x30,0x40,0x50]
        reg_TXBCTRL = [0,0,0]
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
        CANINTF = 0x2C
        CANINTE = 0x2B

        reg_TXBCTRL[buf_num] = self.device_read_data(TXBCTRL[buf_num])#change txbctrl[0] - adr to value
        #CANCTRL[0] = self.device_read_data(CANCTRL[0])
        if (reg_TXBCTRL[buf_num] & 0b01110000) == 0:#check ABTF, MLOA, TXERR, TXREQ, CANCTRL[ABAT]
            print('TXB0CTRL and 0b01110000 = 0')
            
            reg_TXBCTRL[buf_num] = data = self.device_read_data(TXBCTRL[buf_num])
            data &= 0xC0
            priority=0
            data |= priority
            print('adr = 0x%X, data = 0x%X'%(TXBCTRL[buf_num], self.write_reg_and_check(TXBCTRL[buf_num], data)))
            
            if (reg_TXBCTRL[buf_num] & (1<<3)) == 0:#check TXREQ 0 - msg sent
                #TXnIF(CANTINF) doesn't use because TXnIE bits = 0
                print('TXREEQ = 0')
                #break#??
            elif reg_TXBCTRL[buf_num] & (1<<5):#MLOA: Message Lost Arbitration bit: 
                print('MLOA = 1')
                #1 =  Message lost arbitration while being sent
                #0 =  Message did not lose arbitration while being sent
            elif reg_TXBCTRL[buf_num] & (1<<3): #TXERR: Transmission Error Detected bit
                #1 =  A bus error occurred while the message was being transmitted
                # receive interrupts are disabled
                print('TXERR = 1, transmit error')
        
        TXBSIDH = [0x31,0x41,0x51]
        TXBSIDL = [0x32,0x42,0x52]
        self.write_reg_and_check(TXBSIDL[buf_num], (ID & 0x07) << 5)
        self.write_reg_and_check(TXBSIDH[buf_num], ID>>3)

        TXBDLC = [0x35, 0x45, 0x55]
        TXBnD = [0x36, 0x46, 0x56]

        self.write_reg_and_check(TXBDLC[buf_num], lenght)
        for i in range(lenght):#Tx buffer
            self.write_reg_and_check((TXBnD[buf_num]+i), tx_data[0][i]+10)
            
        priority = 0#3 - buf_num
        self.write_reg_and_check(TXBCTRL[buf_num], 
        1<<3 | (priority & 0x03))#TXREQ, 0bXX - priority
              
        print('CAN msg sent')
        
    def can_rx_func(self):
        RXB0CTRL = 0x60
        RXBSIDH = [0x61, 0x71]
        RXBSIDL = [0x62, 0x72]
        RXBDLC = [0x65, 0x75]
        RXBD0 = [0x66, 0x76]
        
        read_rxb0ctrl = self.device_read_data(RXB0CTRL)
        lenght = self.device_read_data(RXBDLC[0])
        rcv_data = []
        for i in range(lenght):
            rcv_data.append(self.device_read_data(RXBD0[0]+i))
        ID = (self.device_read_data(RXBSIDH[0])<<3)|self.device_read_data(RXBSIDL[0])>>5
        print('ID=0x%X, lenght=%d, rcv_data = ' % (ID,lenght), rcv_data)
        print('CAN msg received')
        
        
mcp2515 = spi_to_can_brd_exchange(200)

print('check_errors_rec_tec', mcp2515.check_errors_rec_tec())
mcp2515.set_config_mode(0,0)
#print('loopback mode: ')
#mcp2515.set_loopback_mode(0)
mcp2515.set_normal_mode()
import random
import time
data = [random.randrange(0,0xFF),random.randrange(0,0xFF),random.randrange(0,0xFF),
        random.randrange(0,0xFF),random.randrange(0,0xFF),random.randrange(0,0xFF),
        random.randrange(0,0xFF),random.randrange(0,0xFF)]
mcp2515.can_tx_func(0x111,2,[10,11])
mcp2515.can_rx_func()
mcp2515.spi_close()
print('spi closed')