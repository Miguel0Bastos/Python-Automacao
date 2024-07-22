#Programa para ler uma COIL e um HOLDING REGISTER do CLP LOGO V8

import tkinter as tk
from pyModbusTCP.client import ModbusClient

def ler_dados_modbus():
    c = ModbusClient(host = "192.168.0.1", port=502)
    if not c.open():
        print("Não foi possível conectar ao CLP")
        exit()
    
    resultc = c.read_coils(8192,1)
    resulth = c.read_holding_registers(528,1)

    if resultc and resulth:
        valor1 = resultc[0]
        valor2 = resulth[0]
        return valor1,valor2
    else:
        print("Erro na leitura")
        return None

def atualizar_dados():
    valores_lidos = ler_dados_modbus()
    if valores_lidos:
        valor_label1.config(text = "Coil: {}".format(valores_lidos[0]))
        valor_label2.config(text = "Holding_Register: {}".format(valores_lidos[1]))
    
    root.after(1000,atualizar_dados)

root = tk.Tk()
root.title("Dados Modbus")

valor_label1 = tk.Label(root,text="Valor 1: ")
valor_label1.pack(pady=10)

valor_label2 = tk.Label(root,text="Valor 2: ")
valor_label2.pack(pady=10)

atualizar_dados()

root.mainloop()