import time
import json
import paho.mqtt.client as mqtt
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#################################
# CONDICIONAL PARA SUSCRIBIRSE A 
# AWS DESDE DIFERENTES TOPICOS
# EN LOCAL HACIA DIFERENTES 
# TOPICOS EN AWS IOT CORE
#################################

topic = "topic/subtopic"

# AWS IoT Core Credenciales
CLIENT_ID = "<inserte el client_id o nombre el objeto>"
endpoint = "<inserte el endpoint ejm: a1qbb6z7xxxxxx-ats.iot.us-east-1.amazonaws.com>"
root_ca_path = "AWScredentials/<inserte root-CA.crt>"
cert_file = "AWScredentials/<inserte *.cert.pem>"
key_file = "AWScredentials/<inserte *.>"

# AWS IoT Core MQTT Broker Port
port = 8883

def on_local_message(client, userdata, msg):
    print(f"Mensaje local recibido: {json.loads(msg.payload)}\n")

    mqtt_client.publish(msg.topic, msg.payload.decode(), 0)

def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: " + str(rc))
    client.subscribe("#")


def connect_local():
    local_broker_address = "localhost"
    local_port = 1883
    local_client = mqtt.Client()
    local_client.on_connect = on_connect
    local_client.on_message = on_local_message
    local_client.connect(local_broker_address, local_port)
    local_client.loop_start()

    return local_client

def connect_aws():
    # AWS IoT Core Connection
    mqtt_client = AWSIoTMQTTClient(CLIENT_ID)
    mqtt_client.configureEndpoint(endpoint, port)
    mqtt_client.configureCredentials(root_ca_path, key_file, cert_file)
    #configuracion adicional----
    mqtt_client.configureAutoReconnectBackoffTime(1, 32, 20)
    mqtt_client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    mqtt_client.configureDrainingFrequency(2)  # Draining: 2 Hz
    mqtt_client.configureConnectDisconnectTimeout(10)  # 10 sec
    mqtt_client.configureMQTTOperationTimeout(5)  # 5 sec

    mqtt_client.connect()
    return mqtt_client

if __name__ == "__main__":
    mqtt_client = connect_aws()
    local_client = connect_local()
    

while True:
    time.sleep(1)