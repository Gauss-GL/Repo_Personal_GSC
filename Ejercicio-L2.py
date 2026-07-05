def contar_por_fase(historial, fases):
    nFases = {'LAUNCH PAD':0, 'ASCENT':0, 'APOGEE':0 , 'DESCENT':0,  'PAYLOAD RELEASE':0,  'PROBE RELEASE':0, 'LANDING':0}
    j=historial[0]
    i=0
    while (j<=len(fases)):
        if(j==historial[i]):
            nFases[fases[j]]+=1
            if(i==17): 
                j+=1
            else:
                i+=1
        else:
            j+=1
    return nFases

def fase_mas_larga(conteo, fases):
    max1=0
    max2=0
    for i in range(len(conteo)):
        if(max1<conteo[fases[i]]): 
            max2=fases[i]
            max1=conteo[fases[i]]
    return max2
def mostrar_resumen(historial, fases): 
    nd = contar_por_fase(historial, fases)
    for i in range(len(fases)):
        print(fases[i], ":", nd[fases[i]], "paquetes")
    print("Fase más larga:", fase_mas_larga(nd, fases))

historial = [0,0,0,1,1,1,1,2,3,3,3,3,3,4,5,6,6,6] 
FASES = { 0: 'LAUNCH PAD', 1: 'ASCENT', 2: 'APOGEE', 3: 'DESCENT', 4: 'PAYLOAD RELEASE', 5: 'PROBE RELEASE', 6: 'LANDING' }
mostrar_resumen(historial, FASES)