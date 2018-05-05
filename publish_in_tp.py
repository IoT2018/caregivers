from __future__ import print_function
import paho.mqtt.publish as publish

#channel configuration, ch='prueba'
channelID = "466538"# The ThingSpeak Channel ID.
writeAPIKey = "B9F7J6ZPHG9EQ0ZG"# The Write API Key for the channel.
mqttHost = "mqtt.thingspeak.com"# The Hostname of the ThingSpeak MQTT broker.
mqttUsername = "TSMQTTRpiDemo"# You can use any Username.
mqttAPIKey ="3G7197TE6ZMUC61X"# Your MQTT API Key from Account > My Profile.
tTransport = "websockets"
tPort = 80

topic = "channels/" + channelID + "/publish/" + writeAPIKey # Create the topic string.

#%%

payload = "field1= c400"+"&field2=new patient"#--------->message to send

try:
    publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})

except:
    print ("There was an error while publishing the data.")