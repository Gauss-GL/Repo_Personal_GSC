def mostrarAltitudes(altitudes):
    for i in range (10):
        print("Paquete ",i+1,": ",altitudes[i])
    
def calcularMaximo(altitudes):
   maximo=altitudes[0]
   for i in range (10):
        if(maximo<altitudes[i]):
            maximo=altitudes[i]
   return maximo

def calcularMinimo(altitudes):
    minimo=altitudes[0]
    for i in range (10):
            if(minimo>altitudes[i]):
                minimo=altitudes[i]
    return minimo

def promedio(altitudes):
    total=0
    for i in range (10):
            total=total+altitudes[i]
    return total/10

altitudes=[120.3,345.7,890.1,1450.2,2100.5,3089.3,2800.1,1900.4,500.2,48.6]
mostrarAltitudes(altitudes)
print("La maxima altutud censada fue: ",calcularMaximo(altitudes))
print("La minima altitud censada fue: ", calcularMinimo(altitudes))
print("El promedio de altitudes censadas fue: ", promedio(altitudes))
