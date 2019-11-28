# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# python3

import string
import iotc
from iotc import IOTConnectType, IOTLogLevel, IOTMessageStatus, IOTQosLevel
from random import randint, random, uniform, choice

#
# Credentials FOR DEVICE from you IoT Central App
# DO NOT DISTRIBUTE CODE WITH CREDENTIALS TO PARNTERS & CUSTOMERS!
#
# Insert credentials for non-simulated device that you added 
# to list of devices in your IoT Central App
#

deviceId = "Your Device ID"
scopeId = "Your Scope ID"
deviceKey = "Your Device Key"


# see iotc.Device documentation above for x509 argument sample
iotc = iotc.Device(scopeId, deviceKey, deviceId, IOTConnectType.IOTC_CONNECT_SYMM_KEY)
iotc.setLogLevel(IOTLogLevel.IOTC_LOGGING_ALL)
iotc.setQosLevel(IOTQosLevel.IOTC_QOS_AT_MOST_ONCE)

gCanSend = False
gCounter = 0
state_list = [0, 1]
batterylevel1 = int (1000)
batterylevel2 = int (1000)
batterylevel3 = int (1000)
batterylevel4 = int (1000)
batterylevel5 = int (1000)


def onconnect(info):
  global gCanSend
  print("- [onconnect] => status:" + str(info.getStatusCode()))
  if info.getStatusCode() == 0:
     if iotc.isConnected():
       gCanSend = True

def onmessagesent(info):
  print("\t- [onmessagesent] => " + str(info.getPayload()))

def oncommand(info):
  print("command name:", info.getTag())
  print("command value: ", info.getPayload())

def onsettingsupdated(info):
  print("setting name:", info.getTag())
  print("setting value: ", info.getPayload())

iotc.on("ConnectionStatus", onconnect)
iotc.on("MessageSent", onmessagesent)
iotc.on("Command", oncommand)
iotc.on("SettingsUpdated", onsettingsupdated)

iotc.connect()

while iotc.isConnected():
  iotc.doNext() # do the async work needed to be done for MQTT
  if gCanSend == True:
    if gCounter % 60 == 0:
      gCounter = 0
      print("Sending telemetry...")
      iotc.sendTelemetry("{ \
\"count1\": " + str(randint(0, 8)) + ", \
\"count2\": " + str(randint(0, 8)) + ", \
\"count3\": " + str(randint(0, 8)) + ", \
\"count4\": " + str(randint(0, 8)) + ", \
\"count5\": " + str(randint(0, 8)) + ", \
\"dwelltime1\": " + str(randint(0, 15)) + ", \
\"dwelltime2\": " + str(randint(0, 15)) + ", \
\"dwelltime3\": " + str(randint(0, 15)) + ", \
\"dwelltime4\": " + str(randint(0, 15)) + ", \
\"dwelltime5\": " + str(randint(0, 15)) + ", \
\"temperature1\": " + str(randint(16, 26)) + ", \
\"temperature2\": " + str(randint(16, 26)) + ", \
\"temperature3\": " + str(randint(16, 26)) + ", \
\"temperature4\": " + str(randint(-18, -15)) + ", \
\"temperature5\": " + str(randint(5, 10)) + ", \
\"humidity1\": " + str(randint(15, 50)) + ", \
\"humidity2\": " + str(randint(15, 50)) + ", \
\"humidity3\": " + str(randint(16, 50)) + ", \
\"humidity4\": " + str(randint(10, 40)) + ", \
\"humidity5\": " + str(randint(10, 40)) + ", \
\"batterylevel1\": " + str(int(batterylevel1/10)) + ", \
\"batterylevel2\": " + str(int(batterylevel2/10)) + ", \
\"batterylevel3\": " + str(int(batterylevel3/10)) + ", \
\"batterylevel4\": " + str(int(batterylevel4/10)) + ", \
\"batterylevel5\": " + str(int(batterylevel5/10)) + ", \
\"state\": " + str(choice(state_list)) + "}")

    gCounter += 1
    batterylevel1 -= 0.002
    batterylevel2 -= 0.003
    batterylevel3 -= 0.004
    batterylevel4 -= 0.005
    batterylevel5 -= 0.006
