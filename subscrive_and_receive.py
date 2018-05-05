import time
import paho.mqtt.client as paho
broker="broker.hivemq.com"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))
    
client= paho.Client("client-002")
#Bind functions to callbacks
client.on_message=on_message


print("connecting to broker ", broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("hospital/sensor1")#subscribe


time.sleep(30)
client.disconnect() #disconnect
client.loop_stop() #stop loop