def validar(correo):
    if " " in correo:
        print("Error: El correo contiene espacios.")
    elif "@" not in correo:
        print("Error: Falta la @.")
    elif not (correo.endswith(".com") or correo.endswith(".es")or correo.endswith(".org") or correo.endswith (".net")):
        print("Alerta: Dominio sospechoso.")
    else:
        print("correo verificado y seguro.")
validar("100624817@alumnos.uc3m.es")