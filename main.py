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
    
    
    # CONDICIONALES 
    if opcion == "1":
        print("Su saldo es:")
        print(saldo)
        
    elif opcion == "2":
        deposito = int(input("Monto a depositar: "))
        
        # VALIDACIONES: NO NEGATIVOS
        if deposito <= 0:
            print("Operacion no valida")
        else:
            saldo = saldo + deposito
            listaoperaciones = listaoperaciones + ["Deposito realizado: +" + str(deposito)]
            print("Deposito exitoso")
            
    elif opcion == "3":
        retiro = int(input("Monto a retirar: "))
        
        # VALIDACIONES: NO NEGATIVOS NI QUE SUPEREN EL SALDO
        if retiro <= 0:
            print("Operacion no valida")
        elif retiro > saldo:
            print("Saldo insuficiente")
        else:
            saldo = saldo - retiro
            listaoperaciones = listaoperaciones + ["Retiro realizado: " + str(retiro)]
            print("Retiro exitoso")

            
    elif opcion == "4":
        print("Historial de transacciones:")

        
        # SI LA LISTA DE TRANSACCIONES ESTA VACIA
        if listaoperaciones == []:
            print("No se realizaron transacciones.")

  # BUCLE FOR PARA RECORRER LA LISTA DE OPERACIONES
        for operacion in listaoperaciones:
            print(operacion)
            
        
        print("Saldo final:")
        print(saldo)
        print("Gracias por su tiempo")

           # ESTE IF MANEJA LAS OPCIONES INCORRECTAS
    if opcion != "1":
        if opcion != "2":
            if opcion != "3":
                if opcion != "4":
                    print("Opcion incorrecta. Intente de nuevo.")

