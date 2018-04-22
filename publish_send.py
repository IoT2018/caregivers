import time
import paho.mqtt.client as paho
broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    
client= paho.Client("client-001") 
#Bind functions to callbacks
client.on_message=on_message


print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

print("publishing ")
client.publish("hospital/sensor1","beacon")#publish
time.sleep(5)
client.publish("hospital/sensor1","ciao")#publish
time.sleep(5)
client.publish("hospital/sensor1","ciaoo")#publish
time.sleep(10)
client.publish("hospital/sensor1","ciaooooo")#publish

time.sleep(30)
client.disconnect() #disconnect
client.loop_stop() #stop loop