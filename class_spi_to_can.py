class spi_to_can_brd_exchange:
    def __init__(self, max_speed_khz):
        import RPi.GPIO as GPIO
        #GPIO SET
        import spidev
        self.spi = spidev.SpiDev(0, 0)
        self.spi.mode=0b00
        self.spi.lsbfirst=False
        self.spi.max_speed_hz = max_speed_khz*1000
    
    def spi_close(self):
        self.spi.close()
        #GPIO SET

    def spi_response_data(self, *data):
        #GPIO RESET
        self.response = self.spi.xfer2(data)
        #GPIO SET
        print('Result is: ', self.response)

    def instruction_reset:
        
    def instruction_read:
    def instruction_read_rx_buf:
    def instruction_write:
    def instruction_load_tx_buf:
    def instruction_rts:
    def instruction_read_status:
    def instruction_rx_status:
    def instruction_bit_modify:
        INSTRUCTION_RESET   0xC0
        INSTRUCTION_READ    0x03
        INSTRUCTION_READ_RX_BUF = lambda parameter_list: expression
        INSTRUCTION_WRITE   0x02
        INSTRUCTION_LOAD_TX_BUF = lambda parameter_list: expression
        INSTRUCTION_RTS lambda parameter_list: expression #REQUEST TO SEND
        INSTRUCTION_READ_STATUS 0xA0
        INSTRUCTION_RX_STATUS   0xB0
        INSTRUCTION_BIT_MODIFY  0x05