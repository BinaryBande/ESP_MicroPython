import socket
import io
from htu21d import HTU21D
import IOConfig
# import xml.etree.ElementTree as et

# data = ""


class WebSocket:

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    def __init__(self):
        self.s = socket.socket()
        self.s.bind(self.addr)
        self.s.listen(1)
        print('listening on', self.addr)

        # root = et.fromstring(data)
        # et = et.parse(io.StringIO(data))
        # root = et.getroot()
        # e = root[0][1].text

    def set_html(self):

        # TODO add in while loop! for live tracking
        while True:
            sensor = HTU21D()
            temp = sensor.get_temp()
            hum = sensor.get_hum()
            adcValue = IOConfig.__adcPin.read()
            html = "<!DOCTYPE html>" \
                   "<html><head>\
                    <title>Welcome</title>\
                        </head><body> <h1>ESP8266 Settings</h1>\
                            <p>Temp:" + str(temp) + "C</p>\
                            <p>Hum:" + str(hum) + "%</p>\
                            <p>ADCValue:" + str(adcValue) + "</p>\
                    </body></html>"
            cl, addr = self.s.accept()
            print('client connected from', self.addr)
            cl.send(html)
            cl.close()
