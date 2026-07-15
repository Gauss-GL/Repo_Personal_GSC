import csv
import os
print(f"Directorio de trabajo actual: {os.getcwd()}")
# --- 1. CÓDIGO DE PREPARACIÓN (Ejecutar para crear los datos sucios) ---
datos_crudos = [
    ["TEAM_ID", "TIME", "ALTITUDE"],
    ["1073", "14:00:01", "120.5"],      # Fila perfecta
    ["1073", "14:00:02", "ESTATICA"],   # Fila corrupta (Causará ValueError al convertir a float)
    ["1073", "14:00:03"],               # Fila mocha (Causará IndexError al pedir la posición [2])
    ["1073", "14:00:04", "130.2"]       # Fila perfecta
]

# Creamos el archivo sucio inicial
with open("vuelo_crudo.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(datos_crudos)
print("Archivo 'vuelo_crudo.csv' generado con errores intencionales.\n")


# SOLUCIÓN: LECTURA, ESCRITURA Y FILTRADO SIMULTÁNEO 
filas_rescatadas = 0
filas_basura = 0

print("Iniciando procesamiento Post-Misión...\n")

# El try principal protege contra fallos de archivos (ej. que no exista vuelo_crudo.csv)
try:
    # Podemos abrir DOS archivos al mismo tiempo separándolos por una coma
    with open("vuelo_crudo.csv", "r", encoding="utf-8") as archivo_in, open("reporte_final.csv", "w", newline="", encoding="utf-8") as archivo_out:
        
        lector = csv.reader(archivo_in)
        escritor = csv.writer(archivo_out)
        
        # Leemos y escribimos el encabezado inmediatamente
        encabezados = next(lector)
        escritor.writerow(encabezados)
        
        for numero_fila, fila in enumerate(lector, start=2):
            try:
                # Intentamos extraer el dato de la altitud para validarlo
                # Si la fila está corta, aquí explota con IndexError
                altitud_texto = fila[2] 
                
                # Intentamos convertirlo a número
                # Si dice "ESTATICA", aquí explota con ValueError
                altitud_numero = float(altitud_texto)
                
                # Si sobrevivió a las dos pruebas anteriores, el dato es oro. ¡Lo escribimos!
                escritor.writerow(fila)
                filas_rescatadas += 1
                
            except IndexError:
                print(f"⚠️ Fila {numero_fila} descartada: Paquete incompleto (IndexError)")
                filas_basura += 1
            except ValueError:
                print(f"⚠️ Fila {numero_fila} descartada: Dato corrupto '{altitud_texto}' (ValueError)")
                filas_basura += 1

    print(f"\n Reporte final generado. {filas_rescatadas} paquetes rescatados, {filas_basura} descartados.")

except FileNotFoundError:
    print(" ERROR CRÍTICO: No se encontró el archivo de vuelo crudo para analizar.")