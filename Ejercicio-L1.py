
def econtrar_perdidos(lista):
    a=0
    lista2=[]
    for i in range(15): 
        if a+1 not in lista:
            lista2.append(a+1)
        a+=1
    return lista2
def calcular_porcentaje_p(recibidos, perdidos): 
    p=(perdidos/(recibidos+perdidos))*100
    return p

def mostrar_reporte(lista):
    print("Se recibieron: ", len(lista), "paquetes")
    print("Paquetes recibidos: ", lista)
    print("Los paquetes perdidos fueron: ", econtrar_perdidos(lista))
    print("Que representan el:",f"{calcular_porcentaje_p(len(lista), len(econtrar_perdidos(lista))):.2f}%", "del total de paquetes")

paquetes_recibidos = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 15]
mostrar_reporte(paquetes_recibidos)