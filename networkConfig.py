# Tutorial form https://github.com/lvidarte/esp8266/wiki/MicroPython:-Network-Basics

import network
import settings
import time
import IOConfig
from umqtt.simple import MQTTClient

__ledOn = 'on'
__ledOff = 'off'
__myDeviceAdd = "34.206.242.200"


def set_access_point():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid='ESP8266_100', password='hallo123')


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


# infos: http://mydevices.com/cayenne/docs/cayenne-mqtt-api/#cayenne-mqtt-api-manually-publishing-subscribing
# check infos for cayenne mqtt formats
def mqtt_subscribe(topic, type, unit, value):
    # convert topic and msg into cayenne format
    cayenneTopic = "v1/%s/things/%s/data/%s" % (settings._mqttUsername, settings._mqttClientId, topic)
    cayenneMsg = "%s,%s=%s" % (type, unit, str(value)[:5])

    mqttClient = MQTTClient(client_id=settings._mqttClientId, server=__myDeviceAdd,
                             user=settings._mqttUsername, password=settings._mqttPassword)
    # mqttClient = MQTTClient("umqtt_client", server=settings._raPiIp)
    mqttClient.connect()
    # print(cayenneTopic)
    # print(cayenneMsg)
    time.sleep(0.1)
    mqttClient.publish("%s" % cayenneTopic, "%s" % cayenneMsg)
    mqttClient.disconnect()


def main():
    connect_wifi()


if __name__ == '__main__':
    # main loop start here
    main()
