import class_spi_to_can
mcp2515 = class_spi_to_can.spi_to_can_brd_exchange(2000)
mcp2515.set_config_mode()
mcp2515.set_baudrate(500)
mcp2515.set_normal_mode()