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
        TEC = [0x1C]
        REC = [0x1D]
        ELFG = [0x2D]
        errors_rec_tec = [self.device_read_data(REC), 
                        self.device_read_data(TEC),
                        self.device_read_data(ELFG)]
        return errors_rec_tec

    def set_config_mode(self, bit_rate, filter_num):#not tested
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
        while self.device_read_data(CANSTAT[0]) & 0x80 != 0x80:
            read_buf = self.device_read_data([CANCTRL[0]])
            read_buf &= 0x1F
            read_buf |= 0x80
            self.device_write_byte(CANCTRL[0], [read_buf])#set to config mode
        
        # 500 kbps, Bit rate = 500 
        # Sample point = 75%
        cnf =   [0b11000000, #0xC0
                0b10010001, #0x91
                0b00000001] #0x01
        self.device_write_byte(0x2A, cnf[0])
        self.device_write_byte(0x29, cnf[1])
        self.device_write_byte(0x28, cnf[2])

        #TXRTSCTRL register
        TXRTSCTRL = [0x0D]
        self.device_write_byte(TXRTSCTRL, 0) #I don't use pins for TX req
        #Filter registers
        #check check_btn HERE!!!!
        RXB0CTRL = [0x60]
        RXB1CTRL = [0x70]
        self.device_write_byte(RXB0CTRL, [0])# rx filters don't use default
        self.device_write_byte(RXB1CTRL, [0])

        RXF0SIDH = [0x00]
        RXF0SIDL = [0x01]

        RXF1SIDH = [0x04]
        RXF1SIDL = [0x05]

        RXF2SIDH = [0x08]
        RXF2SIDL = [0x09]

        RXF3SIDH = [0x10]
        RXF3SIDL = [0x11]

        RXF4SIDH = [0x14]
        RXF4SIDL = [0x15]

        RXF5SIDH = [0x18]
        RXF5SIDL = [0x19]

        self.device_write_byte(RXF0SIDH, [0])
        self.device_write_byte(RXF0SIDL, [0])
        
        RXF0EID8 = [0x02]
        RXF0EID0 = [0x03]
        self.device_write_byte(RXF0EID8, [0])
        self.device_write_byte(RXF0EID0, [0])

        #Mask registers
        RXM0SIDH = [0x20]
        RXM0SIDL = [0x21]
        RXM1SIDH = [0x24]
        RXM1SIDL = [0x25]
        self.device_write_byte(RXM0SIDH, [0])
        self.device_write_byte(RXM0SIDL, [0])
        self.device_write_byte(RXM1SIDH, [0])
        self.device_write_byte(RXM1SIDL, [0])

        

    def set_listen_only_mode(self, filter_num):
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
    
    def set_loopback_mode(self, filter_num):#not tested
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]

        while self.device_read_data(CANSTAT[0]) & 0x80 != 0x80:#to config
            read_buf = self.device_read_data([CANCTRL[0]])
            read_buf &= 0x1F
            read_buf |= 0x80
            self.device_write_byte(CANCTRL[0], [read_buf])#set to config mode

        while self.device_read_data(CANSTAT[0]) & 0x40 != 0x40:#to loopback
            read_buf = self.device_read_data([CANCTRL[0]])
            read_buf &= 0x1F
            read_buf |= 0x40
            self.device_write_byte(CANCTRL[0], [read_buf])#set to config mode
        
    #def set_normal_mode(self):

    def can_tx_func(self, buf_num):#haven't wrote yet
        adr = 0x30
        TXBCTRL = [0x30,0x40,0x50]
        while mcp2515.device_read_data(adr) and 0b0100 == True:
            adr += 0x10
            if adr > 0x50:
                adr = 0x30
        #if adr = 0x30


        reg_TXBCTRL = [0,0,0]
        CANCTRL = [0x0F,0x1F,0x2F,0x3F,0x4F,0x5F,0x6F,0x7F]
        CANSTAT = [0x0E,0x1E,0x2E,0x3E,0x4E,0x5E,0x6E,0x7E]
        CANINTF = 0x2C
        CANINTE = 0x2B

        reg_TXBCTRL[0] = mcp2515.device_read_data(TXBCTRL[0])#change txbctrl[0] - adr to value
        CANCTRL[0] = mcp2515.device_read_data(CANCTRL[0])
        if (reg_TXBCTRL[0] & 0b01110000) == 0:#check ABTF, MLOA, TXERR, TXREQ, CANCTRL[ABAT]
            print('TXB0CTRL and 0b01110000 = 0')
            
            reg_TXBCTRL[0] = data = mcp2515.device_read_data(adr)
            data &= 0xC0
            priority=0
            data |= priority
            print('adr = 0x%X, data = 0x%X'%(adr, mcp2515.write_reg_and_check(adr, data)))
            
            if reg_TXBCTRL & (1<<3) == 0:#check TXREQ 0 - msg sent
                #TXnIF(CANTINF) doesn't use because TXnIE bits = 0
                break#??
            elif reg_TXBCTRL & (1<<5):#MLOA: Message Lost Arbitration bit: 
                #1 =  Message lost arbitration while being sent
                #0 =  Message did not lose arbitration while being sent
            elif reg_TXBCTRL & (1<<3): #TXERR: Transmission Error Detected bit
                #1 =  A bus error occurred while the message was being transmitted
                # receive interrupts are disabled
                reg_TXBCTRL
        

mcp2515 = spi_to_can_brd_exchange(1500)

print('write & check data = 0x%X' % mcp2515.write_reg_and_check(0x31, 0xAA))

mcp2515.spi_close()
print('spi closed')