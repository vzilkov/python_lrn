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
    
    def spi_response_data(self, *data):
        self.GPIO.output(nCS_pin, self.GPIO.LOW)
        self.response = self.spi.xfer2(data)
        self.GPIO.output(nCS_pin, self.GPIO.HIGH)
        print('Result is: ', self.response)
    
    def spi_read_data(self):
        self.spi.readbytes(n) #read n bytes from SPI

    
    def device_reset(self):
        self.GPIO.output(self.nCS_pin, self.GPIO.LOW)
        INSTRUCTION_RESET = [0xC0]
        self.spi.writebytes(INSTRUCTION_RESET)
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
    
    def device_read_data(self, adr):#works??
        self.GPIO.output(self.nCS_pin, self.GPIO.LOW)
        
        INSTRUCTION_READ = 0x03
        self.spi.writebytes([INSTRUCTION_READ, adr])
        read_byte = self.spi.readbytes(14)
        
        self.GPIO.output(self.nCS_pin, self.GPIO.HIGH)
        return read_byte
        
    def device_write_byte(self, adr, val):
        INSTRUCTION_WRITE = 0x02
        buf = bytes([INSTRUCTION_WRITE, adr, val])
    
    def read_rx_buf(self):
        self.GPIO.output(nCS_pin, self.GPIO.LOW)
        
        INSTRUCTION_READ_RX_BUF = 0x90 #0x90 - adr 0x61, 0x92 - adr 0x66, 0x94 - adr 0x71, 0x96 - adr 0x76
        self.spi.writebytes(INSTRUCTION_READ_RX_BUF)
        read_byte = self.spi.readbytes(1)
        
        self.GPIO.output(nCS_pin, self.GPIO.HIGH)
        
    '''def instruction_write:
    def instruction_load_tx_buf:
    def instruction_rts:
    def instruction_read_status:
    def instruction_rx_status:
    def instruction_bit_modify:
        
        
        
        
        INSTRUCTION_LOAD_TX_BUF = lambda parameter_list: expression
        INSTRUCTION_RTS lambda parameter_list: expression #REQUEST TO SEND
        INSTRUCTION_READ_STATUS 0xA0
        INSTRUCTION_RX_STATUS   0xB0
        INSTRUCTION_BIT_MODIFY  0x05'''
        
mcp2515 = spi_to_can_brd_exchange(100)

#for i in range(50):
print('memory val = ', (mcp2515.device_read_data(0xf)))
mcp2515.spi_close()