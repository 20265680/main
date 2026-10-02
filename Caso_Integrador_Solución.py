#Sistema de control de colas
print("Bienvenido al sistema ! ")
cola= ["Sofia","Mateo","Valeria"]
retirados=[]
cancelados=[]
print(f"La cola actual es: {cola}")
print("Menu de opciones: ")
print("1. Registrar estudiante regular")
print("2. Registrar estudiante prioritario")
print("3. Cancelar una solicitud")
print("4. Atender al siguiente estudiante")
print("5. Consultar cola")
print("6. Cerrar el sistema")

opcion = input("Ingrese su opción( 1-6): ")
# 1 es numero, "1" es texto
while True: 
    if opcion == "1":
        while True:
            estudiante = input("Digite el nombre del estudiante (Ej. Juan): ")
            if estudiante in cola or estudiante == "":
                print("El valor es invalido")
            else:
                cola.append(estudiante)  # cola.append es mandar al final de la cola
                print(f"La nueva cola es: {cola}")
                cancelados.append(estudiante)  # cancelados es una lista que guarda los estudiantes que se han registrado
                print(f"Los estudiantes que se han registrado son: {cancelados}")
                # f es modificar el texto de lo que esta entre comillas
                break
    elif opcion == "2":
        while True:
            estudiante = input("Digite el nombre del estudiante (Ej. Juan): ")
            if estudiante in cola or estudiante == "":
                print("El valor es invalido")
            else:
                cola.insert(0, estudiante)  # cola.insert es mandar al inicio de la cola
                print(f"La nueva cola es: {cola}")
                cancelados.append(estudiante)  # cancelados es una lista que guarda los estudiantes que se han registrado
                print(f"Los estudiantes que se han registrado son: {cancelados}")
                break
    elif opcion == "3":
        while True:
            estudiante = input("Digite el nombre del estudiante a cancelar (Ej. Juan): ")
            if estudiante in cancelados:
                cancelados.remove(estudiante)
                print(f"El estudiante {estudiante} ha sido cancelado.")
                break
            else:
                print("El estudiante no está en la lista de cancelados.")
    elif opcion == "6": 
        confirmacion = input("¿Está seguro que desea cerrar el sistema? (S/N): ")
        if confirmacion == "S":
            print( "Gracias por venir")
            print(f"la lista actiual es: {cola}")
            break