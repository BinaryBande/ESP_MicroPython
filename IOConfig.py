# Configuration for IO's

import machine

__powerLed = machine.Pin(13, machine.Pin.OUT)
__i2cLed = machine.Pin(15, machine.Pin.OUT)
__adcPin = machine.ADC(0)
__sleepSwitch = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)


def setPowerLED(state):
    if state == 'on':
        __powerLed.on()
    else:
        __powerLed.off()


def i2cLED(state):
    if state == 'on':
        __i2cLed.on()
    else:
        __i2cLed.off()


def main():
    pass


if __name__ == '__main__':
    # main loop start here
    main()
