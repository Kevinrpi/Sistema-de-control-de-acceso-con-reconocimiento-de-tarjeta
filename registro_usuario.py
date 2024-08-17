#Registro nuevo

import os
import sys
import requests
from datetime import datetime
import paho.mqtt.client as mqtt
import json
import RPi.GPIO as gpio
from time import sleep

#Configuarcion inicial 
puerta = 26  #GPIO26
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(puerta,gpio.OUT)
gpio.output(puerta,gpio.LOW)

#Conexion MQTT
client = mqtt.Client()
topic = "Banco/Acceso"
client.connect("35.157.194.143",1883,60)

#Funcion captura imagen
def capture_image(person_name):
    # Define URL para captura de imagen
    capture_url = "http://192.168.1.78/capture"
    
    # Envia un request a ESP32-CAM a capturar imagen
    response = requests.get(capture_url)
    
    if response.status_code == 200:
        # Crea un directorio del usuario en caso de que no exista
        person_dir = f"acceso/{person_name}"
        os.makedirs(person_dir, exist_ok=True)
        
        # Genera el archivo con la hora de captura
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{person_dir}/{person_name}_{timestamp}.jpg"
        
        # Guarda la imagen en el directorio correspondiente
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"IMAGEN CAPTURADA {filename}")
        gpio.output(puerta,gpio.HIGH)
        sleep(3)
        gpio.output(puerta,gpio.LOW)
    else:
        print("ERROR AL CAPTURAR IMAGEN DE ESP32-CAM")
        gpio.output(puerta,gpio.HIGH)
        sleep(0.5)
        gpio.output(puerta,gpio.LOW)

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: python register_person.py <person_name>")
        sys.exit(1)
    
    person_name = sys.argv[1]
    #Filtramos el nombre del archivo para mostrar los datos por separado
    part = person_name.split("_")

    #Asignamos los datos correspondientes
    nombre = part[0]
    tarjeta = part[1]

    #Formato json para publicar
    datos = json.dumps({"nom":nombre,"id":tarjeta,"stu":"REGISTRO NUEVO"})
    client.publish(topic,datos)

    capture_image(person_name)