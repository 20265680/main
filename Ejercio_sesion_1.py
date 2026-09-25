
equipo = input("Equipo (Laptop o Tablet): ")
if equipo == "Laptop":
    horas=int(input("Horas: "))
    if horas < 0:
        print("Solo valores positivos")
    elif horas <= 2:
        print("Poco")
    elif horas <= 5:
        print("Normal")
    elif horas <= 8:
        print("Mucho")
    else: 
        print("No Aplica")
else:
    print("No leyó el programa,trabaja")