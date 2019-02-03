# Tutorial form https://github.com/lvidarte/esp8266/wiki/MicroPython:-Network-Basics

import network
import settings
import time
import IOConfig

__ledOn = 'on'
__ledOff = 'off'


def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(settings._ssid, settings._wifiPassword)
        while not sta_if.isconnected():
            IOConfig.i2cLED(__ledOn)
            time.sleep(0.25)
            IOConfig.i2cLED(__ledOff)
            time.sleep(0.25)
            pass
    print('network config:', sta_if.ifconfig())


def main():
    connect_wifi()


if __name__ == '__main__':
    # main loop start here
    main()
