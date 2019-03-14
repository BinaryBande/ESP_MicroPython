# lib for htu21d
# idea from https://github.com/julianhille/htu21d-esp8266/blob/master/htu21d.py

from machine import I2C, Pin
import time


class HTU21D:

    __DEVICEADRESS = 0x40
    __TEMPADDRESS = 0xE3
    __HUMADRESS = 0xE5

    def __init__(self):

        # TODO: frequency ist very low, because of long wires and solder-points??
        # need to be tested with direct wired pins !
        self.i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

    def _crc_check(self, value):
        """CRC check data
                Notes:
                    stolen from https://github.com/sparkfun/HTU21D_Breakout

                Args:
                    value (bytearray): data to be checked for validity
                Returns:
                    True if valid, False otherwise
                """
        remainder = ((value[0] << 8) + value[1]) << 8
        remainder |= value[2]
        divisor = 0x988000

        for i in range(0, 16):
            if remainder & 1 << (23 - i):
                remainder ^= divisor
            divisor >>= 1

        if remainder == 0:
            return True
        else:
            return False

    def raw_measurement(self, mem_address):
        """
        get the raw data from the mem_address

        :param mem_address:

        :return raw_data:
        """

        self.i2c.start()
        self.i2c.writeto_mem(int(self.__DEVICEADRESS), int(mem_address), '')
        # really important! without pause ETIMEOUT
        time.sleep(0.1)
        self.i2c.stop()
        data = bytearray(3)
        self.i2c.readfrom_into(self.__DEVICEADRESS, data)
        if not self._crc_check(data):
            raise ValueError()
        raw_data = (data[0] << 8) + data[1]
        raw_data &= 0xFFFC
        return raw_data

    def get_temp(self):
        # calculate real temperature from raw-data
        # returns temp
        raw_data = self.raw_measurement(self.__TEMPADDRESS)
        temp = -46.85 + (175.72 * raw_data / 65536)
        return temp

    def get_hum(self):
        # calculate real humidity from raw-data
        # returns hum
        raw_data = self.raw_measurement(self.__HUMADRESS)
        hum = -6 + (125.0 * raw_data / 65536)
        return hum
