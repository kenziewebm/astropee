import requests
import datetime

class SubListener:
  def onItemUpdate(self, update):

    # this function gets ran every time the pee tank capacity changes

    print("urine tank: " + update.getValue("Value"))
    timestamp = datetime.datetime.now().isoformat()
    with open("webhook_url.txt","r") as f:
        url = f.read().strip()
    payload = {
    "username": "astropee",
    "embeds": [
        {
            "color": 16776960, 
            "title": "guys an astronaut just peed i think",
            "description": f"urine tank level: {update.getValue('Value')}",
            "footer": {
                "text": timestamp
            }
        }
    ]
    }
    response = requests.post(url, json=payload)

    pass
  def onClearSnapshot(self, itemName, itemPos):
    pass
  def onCommandSecondLevelItemLostUpdates(self, lostUpdates, key):
    pass
  def onCommandSecondLevelSubscriptionError(self, code, message, key):
    pass
  def onEndOfSnapshot(self, itemName, itemPos):
    pass
  def onItemLostUpdates(self, itemName, itemPos, lostUpdates):
    pass
  def onListenEnd(self):
    pass
  def onListenStart(self):
    pass
  def onSubscription(self):
    pass
  def onSubscriptionError(self, code, message):
    pass
  def onUnsubscription(self):
    pass
  def onRealMaxFrequency(self, frequency):
    pass
