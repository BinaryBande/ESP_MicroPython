# NodeMCU Pinout https://pradeepsinghblog.files.wordpress.com/2016/04/nodemcu_pins.png?w=616
# ESP8266 Micropython Tutorial https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html
# MicroPython Libs https://github.com/pfalcon/micropython-lib
# MicroPython Pycharm Plugin Tutorial https://github.com/vlasovskikh/intellij-micropython
import time
import upip
import machine
import i2c_scanner
import networkConfig
import IOConfig
import os

# Wifi is needed for installing the packages
networkConfig.connect_wifi()

# TODO: test later with list
pkgList = ["micropython-io-0.1.tar.gz", "micropython-xmltok2-0.2.tar.gz",
           "micropython-xml.etree.ElementTree-0.1.1.tar.gz", "micropython-umqtt.simple-1.3.4.tar.gz"]

try:
    f = open('lib/io.py', "r")
    io_exists = True
    f.close()
    print('io.py already installed.')
except OSError:
    io_exists = False
if not io_exists:
    upip.install("micropython-io")

try:
    f = open('lib/xmltok2.py', "r")
    xmltok2_exists = True
    f.close()
    print('xmltok2.py already installed.')
except OSError:
    xmltok2_exists = False
if not xmltok2_exists:
    upip.install("micropython-xmltok2")

try:
    f = open('lib/xml/etree/ElementTree.py', "r")
    xml_exists = True
    f.close()
    print('ElementTree.py already installed.')
except OSError:
    xml_exists = False
if not xml_exists:
    upip.install("micropython-xml.etree.ElementTree")

try:
    f = open('lib/umqtt/simple.py', "r")
    xml_exists = True
    f.close()
    print('umqtt.simple.py already installed.')
except OSError:
    xml_exists = False
if not xml_exists:
    upip.install("micropython-umqtt.simple")

from webSocket import WebSocket
from htu21d import HTU21D


__ledOn = 'on'
__ledOff = 'off'


def main():
    # start Power LED
    sensor = HTU21D()
    temp = sensor.get_temp()
    hum = sensor.get_hum()
    print('Temp: %s°C / Hum: %s%%' % (temp, hum))
    adcValue = IOConfig.__adcPin.read()
    print('adcValue: %s' % adcValue)
    networkConfig.mqtt_subscribe(sensor.get_temp())
    # ws = WebSocket()
    # ws.set_html()
    IOConfig.setPowerLED(__ledOn)
    switchState = IOConfig.__sleepSwitch.value()
    if switchState == 1:
        time.sleep(0.5)
        machine.deepsleep()
    else:
        pass


if __name__ == '__main__':
    # configure rtc für DEEPSLEEP wake up
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    # DEEPSLEEP 0.5 minutes
    rtc.alarm(rtc.ALARM0, 30000)
    # main loop start here
    # get free space
    # https://forum.micropython.org/viewtopic.php?f=16&t=2361&hilit=statvfs
    fs_stat = os.statvfs('/')
    fs_size = fs_stat[0] * fs_stat[2]
    fs_free = fs_stat[0] * fs_stat[3]
    print("File System Size {:,} - Free Space {:,}".format(fs_size, fs_free))
    i2c_scanner.scan()
    # networkConfig.set_access_point()
    main()
