#!/usr/bin/python
from lightstreamer.client import *
from subscription_listener import *

def wait_for_input():
    input("hit enter to stop updates\n")

loggerProvider = ConsoleLoggerProvider(ConsoleLogLevel.WARN)
LightstreamerClient.setLoggerProvider(loggerProvider)

lightstreamer_client = LightstreamerClient("http://push.lightstreamer.com", "ISSLIVE")
lightstreamer_client.connect()

subscription = Subscription(
    mode="MERGE",
    items=["NODE3000005"],
    fields=["Value", "TimeStamp"])
subscription.addListener(SubListener())
lightstreamer_client.subscribe(subscription)

wait_for_input()

lightstreamer_client.unsubscribe(subscription)
lightstreamer_client.disconnect()
