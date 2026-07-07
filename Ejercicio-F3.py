EQUIPO = '1073' # variable global
def contar_resultados(historial):
    status={'OK':0,'ERROR':0}
    for i in range(len(historial)): 
        if (historial[i]['resultado']=='OK'): 
            status['OK']+=1
        else: 
            status['ERROR']+=1
    return status
def buscar_comando(historial, nombre):#"CX,ON"
    comando=[]
    for i in range(len(historial)): 
        if(historial[i]['comando']==nombre): 
            comando.append(historial[i])
    return comando
def mas_usado(historial):
    nombres=[]
    for i in range(len(historial)):
        if (historial[i]['comando'] not in nombres): 
            nombres.append(historial[i]['comando'])
    temp={'CX,ON':0,'CAL':0,'SIM,ENABLE':0,'SIM,ACTIVATE':0,'SIM,DISABLE':0,'CX,OFF':0}
    for i in range(len(historial)):
        a=historial[i]['comando']
        temp[a]+=1 
    max1=temp[nombres[0]]
    max2=nombres[0]
    for i in range(len(nombres)): 
        if(temp[nombres[i]]>max1):
            max1=temp[nombres[i]]
            max2=nombres[i]
    return max2
def mostrar_historial(historial):
    print("--------------Historial de comandos---------------Equipo:", EQUIPO,"-----")
    for i in range(len(historial)):
        print(historial[i]['tiempo'], "|", historial[i]['comando'],"\t|", historial[i]['resultado'])
    res=contar_resultados(historial)
    print("Resultados:\tOK:",res['OK'],"\tERROR:", res['ERROR'])
    print("Comando mas utilizado:", mas_usado(historial))
historial = [ {'comando': 'CX,ON', 'resultado': 'OK', 'tiempo': '00:00:05'}, {'comando': 'CAL', 'resultado': 'OK', 'tiempo': '00:00:12'}, {'comando': 'SIM,ENABLE', 'resultado': 'OK', 'tiempo': '00:01:00'}, {'comando': 'SIM,ACTIVATE', 'resultado': 'OK', 'tiempo': '00:01:05'}, {'comando': 'SIM,DISABLE', 'resultado': 'ERROR','tiempo': '00:03:00'}, {'comando': 'CX,OFF', 'resultado': 'OK', 'tiempo': '00:05:00'}, {'comando': 'CAL', 'resultado': 'ERROR','tiempo': '00:05:30'}, {'comando': 'CX,ON', 'resultado': 'OK', 'tiempo': '00:06:00'} ]

mostrar_historial(historial)