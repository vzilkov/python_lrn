class spi_to_can_brd_exchange:
    import RPi.GPIO as GPIO
    def __init__(self, max_speed_khz):
        self.GPIO.setmode(self.GPIO.BCM)
        self.nCS_pin = 24
        self.GPIO.setup(self.nCS_pin, self.GPIO.OUT)
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
        
        import spidev
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.mode=0b00
        self.spi.lsbfirst=False
        self.spi.max_speed_hz = max_speed_khz*1000

    def spi_close(self):
        self.spi.close()
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
        
    def device_reset(self):#not tested
        self.GPIO.output(self.nCS_pin, self.GPIO.LOW)
        
        INSTRUCTION_RESET = 0xC0
        self.spi.writebytes(INSTRUCTION_RESET)

        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
    
    def device_read_data(self, adr):#not tested
        self.GPIO.output(self.nCS_pin, self.GPIO.LOW)
        
        INSTRUCTION_READ = 0x03
        self.spi.writebytes([INSTRUCTION_READ, adr])
        #read_byte = self.spi.xfer3([hex(adr)], 1, [, self.spi.max_speed_hz, 1, 8])
        read_byte = self.spi.readbytes(1)
        
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
        return read_byte
        
    def device_write_byte(self, adr, val):#not tested
        self.GPIO.output(nCS_pin, self.GPIO.LOW)

        INSTRUCTION_WRITE = 0x02
        buf = [INSTRUCTION_WRITE, hex(adr), hex(val)]
        self.spi.writebytes(buf)

        self.GPIO.output(nCS_pin, self.GPIO.HIGH)
    
    def read_rx_buf(self):#?????????????
        self.GPIO.output(nCS_pin, self.GPIO.LOW)
        
        INSTRUCTION_READ_RX_BUF = 0x90 #0x90 - adr 0x61, 0x92 - adr 0x66, 0x94 - adr 0x71, 0x96 - adr 0x76
        self.spi.writebytes(INSTRUCTION_READ_RX_BUF)
        read_byte = self.spi.readbytes(1)
        
        self.GPIO.output(nCS_pin, self.GPIO.HIGH)
        return read_byte

    def load_tx_buf(self):
        self.GPIO.output(nCS_pin, self.GPIO.LOW)
        INSTRUCTION_LOAD_TX_BUF = 0
        self.GPIO.output(nCS_pin, self.GPIO.HIGH)
        return 1
    
    def req_to_send(self):
        self.GPIO.output(nCS_pin, self.GPIO.LOW)
        INSTRUCTION_RTS = 1
        self.GPIO.output(nCS_pin, self.GPIO.HIGH)
        return 1
    
    def read_status(self): #not tested
        self.GPIO.output(nCS_pin, self.GPIO.LOW)

        INSTRUCTION_READ_STATUS = 0xA0
        self.spi.writebytes(INSTRUCTION_READ_STATUS)
        read_bytes = self.spi.readbytes(2)

        self.GPIO.output(nCS_pin, self.GPIO.HIGH)

        '''if read_bytes[0] == read_bytes[1]:
            return read_bytes[0]
        else:
            return 0xFF #error'''
        return read_bytes

    def read_rx_status(self): #not tested
        self.GPIO.output(nCS_pin, self.GPIO.LOW)

        INSTRUCTION_RX_STATUS = 0xB0
        self.spi.writebytes(INSTRUCTION_RX_STATUS)
        read_bytes = self.spi.readbytes(2)

        self.GPIO.output(nCS_pin, self.GPIO.HIGH)

        '''if read_bytes[0] == read_bytes[1]:
            return read_bytes[0]
        else:
            return 0xFF #error'''
        return read_bytes

    def bit_modify(self, adr_byte, mask_byte, data_byte):
        self.GPIO.output(nCS_pin, self.GPIO.LOW)

        INSTRUCTION_BIT_MODIFY = 0x05
        buf = [INSTRUCTION_BIT_MODIFY, adr_byte, mask_byte, data_byte]
        self.spi.writebytes(buf)

        self.GPIO.output(nCS_pin, self.GPIO.HIGH)

        
mcp2515 = spi_to_can_brd_exchange(100)

print('memory val = ', (mcp2515.device_read_data(0xXF)))
mcp2515.spi_close()