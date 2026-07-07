EQUIPO = 'Cuauhtémoc'
VOLTAJE_NORMAL=7.75
VOLTAJE_MINIMO = 7.65
def obtener_nombre(paquete,m_estados):
    estado=''
    for i in range(len(paquete)):
        if(paquete['estado'] in m_estados):
            estado=paquete ['estado']
        else:
            estado='DESCONOCIDO'
    return estado
def clasifficar_voltaje(voltaje):
    nivel=''
    for i in range (len(paquetes)):
        if(voltaje['voltaje']>=VOLTAJE_NORMAL):
            nivel='NORMAL'
        elif(voltaje['voltaje']<VOLTAJE_NORMAL and voltaje['voltaje']>VOLTAJE_MINIMO):
            nivel='BAJO'
        else:
            nivel='CRITICO'
    return nivel
def calcular_tasa(paquete, npaq):
    transito=''
    if(npaq<1):
        transito='N/A'
    else: 
        if((paquete[npaq-1]['altitud']-paquete[npaq]['altitud']>=0)):
            transito='DESCENSO'
        else: 
            transito='ASCENSO'
    return transito,paquete[npaq-1]['altitud']-paquete[npaq]['altitud']

def mostrar_reporte(paquetes, estados):
    print("----------REPORTE DE VUELO------------",EQUIPO,"--------")
    for i in range(len(paquetes)): 
        transito, delta=calcular_tasa(paquetes, i)
        print("Paquete", paquetes[i]['id'],' | ',estados[obtener_nombre(paquetes[i], estados)], ' | ', 'Voltaje:',clasifficar_voltaje(paquetes[i]), ' | ',transito, ":",delta)
    
def encontrar_apogeo(paquetes):
    max1=0
    max2=0
    for i in range (len (paquetes)):
        if (paquetes[i]['altitud']>max1):
            max1=paquetes[i]['altitud']
            max2=paquetes[i]
    return max2
def contar_alertas(paquetes):
    n_alertas=0
    for i in range (len(paquetes)): 
        if (paquetes[i]['voltaje']<VOLTAJE_NORMAL and paquetes[i]['altitud']>500):
            n_alertas+=1
    return n_alertas 

paquetes = [{'id':1, 'altitud':120.3, 'temp':42.1, 'voltaje':7.80, 'estado':0},{'id':2, 'altitud':890.5, 'temp':41.3, 'voltaje':7.78, 'estado':1},{'id':3, 'altitud':2100.1, 'temp':39.8, 'voltaje':7.75, 'estado':1},{'id':4, 'altitud':3089.3, 'temp':38.2, 'voltaje':7.72, 'estado':2},{'id':5, 'altitud':1500.0, 'temp':39.1, 'voltaje':7.70, 'estado':3},{'id':6, 'altitud':500.2, 'temp':40.5, 'voltaje':7.65, 'estado':3},{'id':7, 'altitud':48.6, 'temp':41.8, 'voltaje':7.60, 'estado':6}]
MAPA_ESTADOS = {0:'LAUNCH PAD', 1:'ASCENT', 2:'APOGEE',3:'DESCENT', 6:'LANDING'}
mostrar_reporte(paquetes,MAPA_ESTADOS)
apogeo=encontrar_apogeo(paquetes)
print("Apogeo encontrado en paquete ",apogeo['id'],':',apogeo['altitud'],"m")
print("Paquetes con alertas:", contar_alertas(paquetes))