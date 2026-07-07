LIMITE_TEMP = 45.0 # variable global — temperatura máxima permitida 
LIMITE_VOLT = 7.60 # variable global — voltaje mínimo permitido
def sensores_activos(lista):
    activos=[]
    for i in range (len(lista)):
        if(lista[i]["activo"]==True):
            activos.append(lista[i]["nombre"])
    return activos
def verificar_alertas(lista):
    for i in range (len(lista)):
        if(lista[i]["nombre"]=="Temperatura" and lista[i]["lectura"]>LIMITE_TEMP):
            print("ALERTA ♥♥♥♥♥: SOBRECALENTAMIENTO")
        elif(lista[i]["nombre"]=="Volaje" and lista[i]["lectura"]>LIMITE_VOLT):
            print("ALERTA ♥♥♥♥♥: SOBREVOLTAJE")
def calcular_stats(lista):
    stats={'total':0, 'activos':0,'con_alerta':0}
    for i in range(len(lista)):
        stats['total']+=1
        if((lista[i]["nombre"]=="Temperatura" and lista[i]["lectura"]>LIMITE_TEMP) or (lista[i]["nombre"]=="Volaje" and lista[i]["lectura"]>LIMITE_VOLT)): 
            stats['con_alerta']+=1
        if(lista[i]["activo"]==True):
            stats['activos']+=1   
    return(stats)
def mostra_panel(lista): 
    print("---------SENSORES---------")
    act=sensores_activos(lista)
    for i in range (len(lista)):
        print(lista[i]['nombre'], "[", lista[i]['activo'],"]",":", lista[i]['lectura'], lista[i]['unidad'])
    verificar_alertas(lista)
    stats=calcular_stats(lista)
    print("Total de sensores",stats['total'])
    print("Sensores activos",stats['activos'])
    print("Alertas",stats['con_alerta'])
sensores = [ {'nombre': 'Barometro', 'unidad': 'kPa', 'lectura': 85.3, 'activo': True }, {'nombre': 'Temperatura', 'unidad': 'C', 'lectura': 46.2, 'activo': True }, {'nombre': 'GPS', 'unidad': 'coord','lectura': 38.37, 'activo': True }, {'nombre': 'Voltaje', 'unidad': 'V', 'lectura': 7.55, 'activo': True }, {'nombre': 'Giroscopio', 'unidad': 'deg/s','lectura': 2.1, 'activo': False}, {'nombre': 'Acelerometro', 'unidad': 'm/s2', 'lectura': 9.85, 'activo': True }, ]
mostra_panel(sensores)
"""for i in range (len(sensores)-len(act)):
        if(sensores[i]['nombre'] not in act): 
            print(sensores[i]['nombre'],"[", lista[i][act[i]],"]",":", lista[i]['lectura'], lista[i]['unidad'])"""