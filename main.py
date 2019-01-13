import time
import machine
import i2c_scanner
import networkConfig
import os


def main():
    # just a little blinki for testing
    led = machine.Pin(2, machine.Pin.OUT)
    while True:
        led.off()
        time.sleep(1)
        led.on()
        time.sleep(1)


if __name__ == '__main__':
    # main loop start here
    i2c_scanner.scan()
    networkConfig.connect_wifi()
    main()
