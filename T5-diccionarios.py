def estado(n, mapa):
    if(n not in mapa):
        return "Estado Invalido"
    else:
        return n
    
def mensaje(estado, fase): 
    if (estado=="Estado Invalido"): 
        print("Numero fuera de rango")

    if (estado in fase):
        print("Active flight")

    if(estado not in fase and estado!="Estado Invalido"):
        print("On ground")

ACTIVE_FLIGHT=[1,2,3]
STATE_MAP={0:"LAUNCH PAD", 1:"ASCEND", 2: "APOGEE",3:"DESCENT", 4:"PAYLOAD RELEASE", 5: "PROBE RELEASE", 6:"LANDING"}  
n=int(input("Ingresa la etapa que quieres analizar: "))
mensaje(estado(n, STATE_MAP), ACTIVE_FLIGHT)
