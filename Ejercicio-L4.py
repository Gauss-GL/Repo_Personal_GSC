def bubble_sort(lista):
    may=0
    men=0
    for i in range(len(lista)):
        for i in range(len (lista)-1):
            if (lista[i+1]>=lista[i]):
                may=lista[i+1] #may
                men=lista[i] #men
                lista[i]=may
                lista[i+1]=men
    return lista
def bubble_inverso(lista):
    may=0
    men=0
    ordinv=[]
    for i in range(len(lista)):
        for i in range(len (lista)-1):
            if (lista[i+1]>=lista[i]):
                may=lista[i+1] #may
                men=lista[i] #men
                lista[i]=may
                lista[i+1]=men

    for i in range(len(lista)-1,-1,-1):
        ordinv.append(lista[i])

    return ordinv
def mostrar(lista): 
    original=lista.copy()
    ordenada=bubble_sort(lista)
    ordenadainv=bubble_inverso(lista)
    print("Lista original:", original)
    print("Lista ordenada:", ordenada)
    print("Lista ordenada invertida:",ordenadainv)

altitudes = [500.2, 3089.3, 120.3, 1900.4, 890.1,2100.5, 48.6, 345.7, 2800.1, 1450.2]
mostrar(altitudes)