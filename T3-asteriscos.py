print("   Bienvenido a este programa, crea una piramide de asteriscos")
n=int (input("Ingresa cuantos renglones vas a querer?"))
j=0
for i in range (n):
    j=j+1
    for i in range (j):
        print("*", end="")  
    print("")
