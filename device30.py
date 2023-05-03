import paho.mqtt.client as mqtt
import time
import json

DEVICE = 'Device 30'
topic = "local/device30"
ping = f"...ping {DEVICE} local..."

def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(DEVICE+" "+msg.topic+" "+msg.payload.decode())

broker_address = "localhost"
port = 1883

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address,port) #agregar mosquitto

contador = 0

client.loop_start()

while True:
    contador += 1
    time.sleep(3)
    message = {"contador": contador, "ping": ping}
    json_message = json.dumps(message)
    client.publish(topic, json_message)
