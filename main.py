print("BIENVENIDO A TU CAJERO AUTOMATICO")
# VARIABLES
saldo = 1000
listaoperaciones = [] # LISTA PARA GUARDAR EL HISTORIAL DE TRANSACCIONES

# BUCLE CON WHILE
opcion = "0"

while opcion != "4":
    
    print("Menú del cajero")
    print("1. Consultar saldo actual")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    
    opcion = input("Seleccione una opcion: ")
