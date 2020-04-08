import spidev

spi_ch = 0

spi = spidev.SpiDev(0,0)

#spi.open()
spi.mode=0b00
spi.lsbfirst=False
spi.max_speed_hz = 1200000

response = spi.xfer2([0x40,0x41,0x42,0x43])
print('Result is: ', response)
spi.close()