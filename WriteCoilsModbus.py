#Programa que escreve em 3 coils no CoDeSys
#Imporar Módulos
import tkinter as tk
from pyModbusTCP.client import ModbusClient

def escrever_coils():
    c = ModbusClient(host="192.168.0.1", port=502)

    if not c.open():
        print("Não foi possível conectar ao Raspberry Pi")
        return False

    #Obter os estados dos três coils da interface gráfica
    estado_coil1 = int(coil1_var.get())
    estado_coil2 = int(coil2_var.get())
    estado_coil3 = int(coil3_var.get())

    #Escrever os estados nos coils nos endereços 0, 1 e 2
    c.write_single_coil(0, estado_coil1)
    c.write_single_coil(1, estado_coil2)
    c.write_single_coil(2, estado_coil3)

    print("Estado dos coils escritos com sucesso")

    #Agendar a próxima escrita após 1000 milisegundos (1 segundo)
    root.after(100, escrever_coils)

#Criar a janela principal
root = tk.Tk()
root.title("Painel de comando Coils Raspberry")

#Variáveis para armazenar o estado dos coils
coil1_var = tk.StringVar(value="0")
coil2_var = tk.StringVar(value="0")
coil3_var = tk.StringVar(value="0")

#Rótulos e botões para cada coil
tk.Label(root, text="Coil 1:").grid(row=0, column=0, padx=10, pady=5)
tk.Checkbutton(root, variable=coil1_var, onvalue="1", offvalue="0").grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Coil 2:").grid(row=1, column=0, padx=10, pady=5)
tk.Checkbutton(root, variable=coil2_var, onvalue="1", offvalue="0").grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Coil 3:").grid(row=2, column=0, padx=10, pady=5)
tk.Checkbutton(root, variable=coil3_var, onvalue="1", offvalue="0").grid(row=2, column=1, padx=10, pady=5)

#Botão para escrever os estados dos coils
tk.Button(root, text="Iniciar Escrita", command=escrever_coils).grid(row=3, column=0, columnspan=2, pady=10)

#Iniciar o loop principal da interface gráfica
root.mainloop()
