# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# python3

import iotc
from iotc import IOTConnectType, IOTLogLevel
from random import randint, random, uniform, choice
import time

#
# Credentials FOR DEVICE from you IoT Central App
# DO NOT DISTRIBUTE CODE WITH CREDENTIALS TO CUSTOMERS!
#
# Instert credentials for non-simulated your device that you added 
# to list of devices in your in-store-analytics IoT Central App
#

deviceId = "your device id"
scopeId = "your scope id"
deviceKey = "your device key"

iotc = iotc.Device(scopeId, deviceKey, deviceId, IOTConnectType.IOTC_CONNECT_SYMM_KEY)
iotc.setLogLevel(IOTLogLevel.IOTC_LOGGING_API_ONLY)

gCanSend = False
gCounter = 0
battery = int (1000)

def onconnect(info):
  global gCanSend
  print("- [onconnect] => status:" + str(info.getStatusCode()))
  if info.getStatusCode() == 0:
     if iotc.isConnected():
       gCanSend = True

def onmessagesent(info):
  print("\t- [onmessagesent] => " + str(info.getPayload()))

def oncommand(info):
  print("- [oncommand] => " + info.getTag() + " => " + str(info.getPayload()))

def onsettingsupdated(info):
  print("- [onsettingsupdated] => " + info.getTag() + " => " + info.getPayload())

iotc.on("ConnectionStatus", onconnect)
iotc.on("MessageSent", onmessagesent)
iotc.on("Command", oncommand)
iotc.on("SettingsUpdated", onsettingsupdated)

iotc.connect()

while iotc.isConnected():
  iotc.doNext() # do the async work needed to be done for MQTT
  if gCanSend == True:
    if gCounter % 30 == 0:
      gCounter = 0
      print("Sending telemetry..")
      iotc.sendTelemetry("{ \
\"temperature\": " + str(randint(18, 25)) + ", \
\"humidity\": " + str(randint(20, 70)) + ", \
\"battery\": " + str(int(battery/10)) + "}")

    gCounter += 1
    battery -= 0.002
