import csv

# --- Código de preparación (Ejecuta esto para crear el archivo sucio) ---
datos_crudos = [
    ["TEAM_ID", "MISSION_TIME", "STATE", "ALTITUDE"],
    ["1073", "00:01:00", "2", "150.5"],     # Válido
    ["1073", "00:01:01", "TRES", "155.0"],  # Estado corrupto (ValueError natural al hacer int)
    ["1073", "00:01:02", "4", "ERROR"],     # Altitud corrupta (ValueError natural al hacer float)
    ["1073", "00:01:03", "4", "165.2"]      # Válido
]
with open("raw_telemetry.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(datos_crudos)
print("Archivo 'raw_telemetry.csv' generado \n")
filas_rescatadas = 0
filas_basura = 0
try:
    with open("raw_telemetry.csv", "r", encoding="utf-8") as archivo_in, open("clean_telemetry.csv", "w", newline="", encoding="utf-8") as archivo_out:   
        lector = csv.reader(archivo_in)
        escritor = csv.writer(archivo_out)
        # Leemos y escribimos el encabezado inmediatamente
        encabezados = next(lector)
        escritor.writerow(encabezados)
        for numero_fila, fila in enumerate(lector, start=2):
            try:
                estado=int(fila[2])
                altitud=float(fila[3])
                escritor.writerow(fila)
                filas_rescatadas+=1
            except ValueError:
                print("La fila",numero_fila, "recuperada no es valida")
                filas_basura+=1
        print("Reporte generado,",filas_rescatadas,"utiles,",filas_basura,"descartadas")
        import os
        print(os.path.abspath("clean_telemetry.csv"))
except FileNotFoundError:
    print(" ERROR CRÍTICO: No se encontró el archivo de vuelo crudo para analizar.")