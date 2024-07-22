#Exemplo de programa para ler 2 registradores em Pyton

from pyModbusTCP.client import ModbusClient
import time

#Criar função Ler_status
def ler_dados_modbus():
    client1 = ModbusClient(host = "192.168.0.1", port = 502)
    client2 = ModbusClient(host = "192.168.0.2", port = 502)
    if not client1.open():
        print('Não foi possível conectar ao CLP 1')
        exit()
    if not client2.open():
        print('Não foi possível conectar ao CLO 2')
        exit()
    
    result = client1 and client2.read_holding_registers(528)
    if result:
        valor1, valor2 = result[0]
        return valor1, valor2
    else:
        print ("Erro na leitura")
        return None
    
def atualizar_dados():
    while True:
        valores_lidos = ler_dados_modbus()
        if valores_lidos is not None:
            print("Valor 1 e 2:", valores_lidos)

        time.sleep(5)

atualizar_dados()

