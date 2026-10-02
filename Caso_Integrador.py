#Practica para que sofia se muera pronto
cola = ["Sofia","Mateo","Valeria"]
print("Cola actual: ", cola)

menu = input("Ingrese su opción [1. Regular, 2. Prioritario, 3. Cancelar una solicitud, 4. Atender al siguiente estudiante, 5. Consultar cola, 6. Cerrar el sistema]:")
while True:
    elif menu == "1":
        Registro = input("Ingrese su carnet: ")
        if Registro in cola:
            print("Su carnet ya está en la cola.")
        else:
            cola.append(Registro)
            print("Cola actual: ", cola)
            
    elif menu == "2":
        Registro = input("Ingrese su carnet: ")
        if Registro in cola:
            print("Su carnet ya está en la cola.")
        else:
            cola.insert(0, Registro)
            print("Cola actual: ", cola)
            
    elif menu == "3":
        Registro = input("Ingrese su carnet: ")
        if Registro in cola:
            cola.remove(Registro)
            print("Su carnet ha sido eliminado de la cola.")
        else:
            print("Su carnet no se encuentra en la cola.")
    elif menu == "4":
        if 
    elif menu == "6":
        break