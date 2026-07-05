EQUIPO = '1073'
COMANDOS_VALIDOS = ['CX,ON', 'CX,OFF', 'CAL', 'SIM,ENABLE', 'SIM,ACTIVATE', 'SIM,DISABLE']

def validar_formato(cmd):
    partes = cmd.split(',')
    if len(partes) >= 3 and partes[0] == 'CMD' and partes[1] == EQUIPO:
        return True
    return False

def extraer_instruccion(cmd):
    if not validar_formato(cmd):
        return 'INVALIDO'
    partes = cmd.split(',')
    return ','.join(partes[2:])

def es_instruccion_conocida(instruccion):
    return instruccion in COMANDOS_VALIDOS

def procesar_todos(lista):
    for cmd in lista:
        if validar_formato(cmd):
            instruccion = extraer_instruccion(cmd)
            conocida = es_instruccion_conocida(instruccion)
            print(f"Comando:", cmd ,"| Válido | Instrucción:",instruccion, "| Conocida" )
        else:
            print(f"Comando:", cmd,"| Invalido | Instrucción: INVALIDO | Desconocido")

comandos_recibidos = [ 'CMD,1073,CX,ON', 'CMD,1073,CAL', 'CMD,9999,CX,ON','CMD,1073,SIM,ENABLE', 'cmd,1073,CAL', 'CMD,1073,SIM,ACTIVATE','CMD,1073,SIM,DISABLE', 'DATOS,1073,OK']

procesar_todos(comandos_recibidos)