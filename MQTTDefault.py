#Programa para publicar dados via MQTT
#Importar Módulos
import paho.mqtt.client as mqtt
import time

#Defina as informações do broker MQTT e as credencias
broker_address = "192.168.0.71"
broker_port = 1883
topic_publish = "status/broker"
client_id = "ClientPython"
username = "pypc"
password = "PythonClient"

#Criar um client MQTT
client = mqtt.Client(client_id)

#Configure as credenciais
client.username_pw_set(username, password)

#Conectar ao broker MQTT
client.connect(broker_address, broker_port, 60)

#Publicar a mensagem a cada 15 segundos
try:
    while True:
        client.publish(topic_publish, " Pytho ON")
        time.sleep(15)
except KeyboardInterrupt:
    print("Desconectando do broker MQTT...")
    client.disconnect()
    print("Programa encerrado.")

    
