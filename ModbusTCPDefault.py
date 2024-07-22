#Programa que lê um registrador em Python. Deafult

#Importação de Módulos
from pyModbusTCP.client import ModbusClient
import time

#Definição da Função ler_dados_modbus
def ler_dados_modbus():
    client1 = ModbusClient(host="192.168.0.1", port=502 ) #IP do CLP que eu quero me conectar
    if not client1.open():
        print('Não foi possível conectar ao CLP')
        exit()
#Ler Registrador (Holding) do CLP
    result = client1.read_holding_registers(529) #Lendo Holding Register n°529 (Esse valor consulta-se na tabela modbus do CLP)
    if result:
        #Obter o valor lido no registrador
        valor1 = result[0]
        return valor1
    else:
        print("Erro na Leitura")
        return  None

def atualizar_dados():
    while True:
        valores_lidos = ler_dados_modbus()

        if valores_lidos is not None:
            print("Valor 1:",valores_lidos)
        
        time.sleep(2)

#Iniciar a leitura de dados
atualizar_dados()

