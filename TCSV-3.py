import csv
datos_secuencia = [
    ["ID", "CMD"],
    ["1", "SYS_CHECK"],
    ["2"],                # ¡Fila incompleta! Faltan datos
    ["3", "CALIBRATE"],
    [],                   # ¡Fila totalmente vacía!
    ["5", "GO"]
]
with open("sequence.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(datos_secuencia)
print("Archivo 'sequence.csv' generado \n")
with open("sequence.csv", "r", encoding="utf-8") as archivo_in, open("csequence.csv", "w", newline="", encoding="utf-8") as archivo_out:
    lector = csv.reader(archivo_in)
    escritor = csv.writer(archivo_out)
    encabezados = next(lector)
    escritor.writerow(encabezados)
    for nfila, fila in enumerate(lector):
        try:
            comando=fila[1]
            escritor.writerow(fila)
        except IndexError:
            print("ALERTA: COMANDO NO DETECTADO")
    print("Archivo 'csequence.csv' generado correctamente")
    import os
    print(os.path.abspath("csequence.csv"))