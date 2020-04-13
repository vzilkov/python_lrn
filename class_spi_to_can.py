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
        return read_byte
        
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


mcp2515 = spi_to_can_brd_exchange(1000)
mcp2515.device_write_byte(0x31, 0xAA)

print('memory val = ', mcp2515.device_read_data(0x31))
print('read_status = ', mcp2515.read_status())
print('read_rx_status = ', mcp2515.read_rx_status())
mcp2515.spi_close()
'''import time
while True:
    mcp2515.cs_low()
    print('gpio low')
    time.sleep(0.5)
    mcp2515.cs_high()
    print('gpio high')
    time.sleep(0.5)'''
    