SIZE_VENTANA=3
def promedio_ventana(lista, inicio): 
    tot=0
    for i in range(inicio, inicio+SIZE_VENTANA):
        tot=lista[i]+tot
    return tot/SIZE_VENTANA

def detectar_tendencia(promedios):
    for i in range(len(promedios)-1):
        if (promedios[i]=='N/A' or i!=len(promedios)-2):
            tendencia=''
        elif(promedios[3]==promedios[i+1]):
                tendencia='ESTABLE'
        elif(promedios[3]<promedios[i+1]):
                tendencia='CALENTANDO'
        elif(promedios[3]>promedios[i+1]):
                tendencia='ENFRIANDO'
    return tendencia

def calcular_promedios_moviles(lista):
    p_moviles=[]
    for i in range(len(lista)):
        if (i-SIZE_VENTANA<0): 
            p_moviles.append('N/A')
        else:
            p_moviles.append(promedio_ventana(lista, i-SIZE_VENTANA))
    print("Lista de promedios:",p_moviles)
    print("La tendencia es:",detectar_tendencia(p_moviles))

temperaturas = [42.1, 41.8, 41.3, 40.5, 39.8, 38.9, 38.2, 38.5, 39.1, 40.2, 41.0, 41.5]
calcular_promedios_moviles(temperaturas)