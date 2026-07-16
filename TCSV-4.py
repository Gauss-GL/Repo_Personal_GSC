
import csv
ejemplo_headers=["Team ID","Mission_time", "Altitude"]
# --- Código de preparación (Simulamos los paquetes llegando por radio) ---
paquetes_entrantes = [
    {"team_id": "1073", "mission_time": "00:01", "altitude": 120.5},
    {"team_id": "1073", "mission_time": "00:02", "altitude": 125.0},
    {"team_id": "1073", "mission_time": "00:03"}, # ¡Paquete incompleto! Falta la altitud
    {"team_id": "1073", "mission_time": "00:04", "altitude": 130.2}
]
with open("flight_log.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow(ejemplo_headers)
print("Archivo 'flight_log.csv' generado \n")
with open("flight_log.csv", "a", newline="", encoding="utf-8") as f:
    escritor=csv.writer(f)
    for i in range(len(paquetes_entrantes)):
        try:
            temp=[paquetes_entrantes[i]['team_id'], paquetes_entrantes[i]['mission_time'], paquetes_entrantes[i]['altitude']]
            escritor.writerow(temp)
        except KeyError:
            print("Paquete",i+1,"con datos perdidos")
import os
print(os.path.abspath("flight_log.csv"))