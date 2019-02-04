# NodeMCU Pin out https://pradeepsinghblog.files.wordpress.com/2016/04/nodemcu_pins.png?w=616
# ESP8266 Micropython Tutorial https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html
import time
import machine
import i2c_scanner
import networkConfig
import IOConfig
import os
from htu21d import HTU21D

__ledOn = 'on'
__ledOff = 'off'


def main():
    # start Power LED
    IOConfig.setPowerLED(__ledOn)
    sensor = HTU21D()
    temp = sensor.get_temp()
    hum = sensor.get_hum()
    print('Temp: %s°C / Hum: %s%%' % (temp, hum))
    adcValue = IOConfig.__adcPin.read()
    print('adcValue: %s' % adcValue)
    machine.deepsleep()


if __name__ == '__main__':
    # configure rtc für DEEPSLEEP wake up
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, 30000)
    # main loop start here
    # get free space
    # https://forum.micropython.org/viewtopic.php?f=16&t=2361&hilit=statvfs
    fs_stat = os.statvfs('/')
    fs_size = fs_stat[0] * fs_stat[2]
    fs_free = fs_stat[0] * fs_stat[3]
    print("File System Size {:,} - Free Space {:,}".format(fs_size, fs_free))
    i2c_scanner.scan()
    networkConfig.connect_wifi()
    main()
