import csv

# --- Código de preparación (Solo creamos 2 de los 3 archivos a propósito) ---
with open("sensor_a.csv", "w", newline="") as f: 
    csv.writer(f).writerows([["TEMP"], [25.5], [26.0]])
with open("sensor_c.csv", "w", newline="") as f: 
    csv.writer(f).writerows([["TEMP"], [24.1], [24.8]])
# sensor_b.csv NO EXISTE simulando un fallo de hardware
print("Archivos de sensores generados \n")
archivos=["sensor_a.csv","sensor_b.csv","sensor_c.csv"]
total=0
n_sensores=0
for archivo in archivos:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lector=csv.reader(f)
            next(lector)
            for fila in lector:
                total+=float (fila[0])
                n_sensores+=1
    except FileNotFoundError:
        print("⚠️ ⚠️ ⚠️ ⚠️ ⚠️  Advertencia,",archivo,"no existe ⚠️ ⚠️ ⚠️ ⚠️ ⚠️")

try:
    promedio=total/n_sensores
    print("El promedio de los datos recuperados es:", promedio)
except ZeroDivisionError:
    print("Sin datos disponibles")
