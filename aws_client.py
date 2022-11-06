import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc): # func for making connection
	print("Connected to MQTT")
	print("Coonection returned result: " + str(rc))

	client.subscribe("mqtt")

def on_message(client, userdata, msg): #func for sending message
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
