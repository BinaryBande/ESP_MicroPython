import time
import machine


def main():
    # just a little blinki for testing
    led = machine.Pin(2, machine.Pin.OUT)
    while True:
        led.off()
        time.sleep(1)
        led.on()
        time.sleep(1)


if __name__ == '__main__':
    # Scanner i2c en MicroPython | MicroPython i2c scanner
    # Renvoi l'adresse en decimal et hexa de chaque device connecte sur le bus i2c
    # Return decimal and hexa adress of each i2c device
    # https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

    # https://gist.github.com/projetsdiy/f4330be62589ab9b3da1a4eacc6b6b1c

    import machine

    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

    print('Scan i2c bus...')
    devices = i2c.scan()

    if len(devices) == 0:
        print("No i2c device !")
    else:
        print('i2c devices found:', len(devices))

        for device in devices:
            print("Decimal address: ", device, " | Hexa address: ", hex(device))

    # main loop start here
    main()
