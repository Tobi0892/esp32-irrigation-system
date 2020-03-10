import gc
import json
from time import sleep
from ntptime import settime

import esp
import network
from machine import reset

esp.osdebug(None)
gc.collect()

with open("config.json", "r") as config:
    config = json.load(config)


def connectWifi():
    print("")
    print("Connecting to WiFi...", end="")

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.config(dhcp_hostname=config["hostname"])
    wifi.connect(
        config["wifi"]["ssid"],
        config["wifi"]["password"]
    )

    while not wifi.isconnected():
        pass

    print("connected")


try:
    connectWifi()
    settime()

except(RuntimeError, TypeError, NameError):
    sleep(60)
    reset()
