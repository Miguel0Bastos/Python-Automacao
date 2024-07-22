#Leitura de dados via OPC UA para Power Panel C70 B&R
#Importação dos Módulos
from opcua import Client
import time

#Endereço do servidor OPC UA do CLP
server_url = "opc.tcp://192.168.0.70:4840"

#Lista de caminhos dos nós que você deseja ler
node_paths = [
    "ns=6;s=::OpcUAServe:ipy01",
    "ns=6;s=::OpcUAServe:ipy02",
    "ns=6;s=::OpcUAServe:rpy01",
    "ns=6;s=::OpcUAServe:rpy02",
    "ns=6;s=::OpcUAServe:spy01",
    "ns=6;s=::OpcUAServe:spy02",

]

#Crie um client OPC UA
client = Client(server_url)

try:
    #Conect-se ao servidor OPC UA
    client.connect()

    while True:
        for node_path in node_paths:
            #Obtenha o nó correspondente
            node = client.get_node(node_path)

            #Leia o valor do nó
            value = node.get_value()

            #Imprima o valor lido
            print("Valor do nó {}: {}".format(node_path, value))

        #Aguardar 5 segundos antes da próxima leitura
        time.sleep(5)
except KeyboardInterrupt:
    #Encerrado pelo usuário usando Ctrl+C
    pass
finally:
    #Desconecte-se do servidor OPC UA
    client.disconnect()
    
