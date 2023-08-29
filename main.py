import json
import time
from datetime import datetime
from whatsapp_api_client import API

id = "1101778445"
token = "cb49bdc0829841e092771f4ad059ed277784102bdaba4bbe93"
activateApi = API.GreenApi(id, token)

def main():
    def onEvent(typeWebhook, body):
       if typeWebhook == 'incomingMessageReceived':
          onIncomingMessageReceived(body)   
             
    def onIncomingMessageReceived(body):
        #idMessage = body['idMessage']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        senderData = body['senderData']
        messageData = body['messageData']
        print(json.dumps(senderData))
        print(str(eventDate))
        print(json.dumps(messageData))
        chatId = senderData['chatId']
        print("##################")
        chatId = senderData['chatId']
        sender = senderData['sender']
        sName = senderData['senderName']
        msg = f"Hey {sName}\nAmeer's currently offline 🌑\n\n_*His assistant meera ✍️✍️*_"
        response = activateApi.sending.sendMessage(sender,msg)
        print(response.data)
        print('hi')

    activateApi.webhooks.startReceivingNotifications(onEvent)   
if __name__ == "__main__":
       main()
    
