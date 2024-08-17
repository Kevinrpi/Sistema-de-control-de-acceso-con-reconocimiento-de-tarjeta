# Registro de entrada

#importamos librerias 
import os
import requests
from deepface import DeepFace
from datetime import datetime
import paho.mqtt.client as mqtt
import json
import RPi.GPIO as gpio
from time import sleep

#Configuarcion 
puerta = 26  #GPIO26
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(puerta,gpio.OUT)
gpio.output(puerta,gpio.LOW)

#Conexion MQTT
client = mqtt.Client()
topic = "Banco/Acceso"
client.connect("35.157.194.143",1883,60)

#Funcion capturar imagen
def capture_image():
    # Define URL para captura de imagen
    capture_url = "http://192.168.1.78/capture"
    
    # Envia un request a ESP32-CAM a capturar imagen
    response = requests.get(capture_url)
    
    if response.status_code == 200:
        # Genera el archivo con fecha y hora de captura
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Img_Registradas/{timestamp}.jpg"
        
        #Guarda las imagenes generadas en una carpeta
        os.makedirs("Img_Registradas", exist_ok=True)
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Image captured and saved to {filename}")
        return filename
    else:
        print("Failed to capture image from ESP32-CAM")
        return None

def compare_faces(captured_image_path):
    database_path = "acceso"
    recognized = False
    
    # Iteracion en cada carpeta de cada registro
    for person_name in os.listdir(database_path):
        person_dir = os.path.join(database_path, person_name)
        
        if os.path.isdir(person_dir):
            # Iteracion en los archivos de de la persona en especifico 
            for img_file in os.listdir(person_dir):
                img_path = os.path.join(person_dir, img_file)
                
                # Compara la imagen capturada con el registro en la carpeta del usuario
                try:
                    result = DeepFace.verify(captured_image_path, img_path, enforce_detection=False)
                    if result["verified"]:
                        print(f"Person recognized as {person_name}")
                        recognized = True
                        gpio.output(puerta,gpio.HIGH)
                        sleep(3)
                        gpio.output(puerta,gpio.LOW)
                        # Mostramos los datos del usuario en NodeRED ya filtrados
                        part = person_name.split("_")

                        #Asignamos los datos correspondientes
                        nombre = part[0]
                        tarjeta = part[1]
                        

                        #Formato json para publicar
                        datos = json.dumps({"nom":nombre,"id":tarjeta,"stu":"ENTRADA"})
                        client.publish(topic,datos)
                        break
                except Exception as e:
                    print(f"Error comparing images: {e}")
                    continue
        
        if recognized:
            break
    
    if not recognized:
        print("Person not recognized in the database")
        gpio.output(puerta,gpio.HIGH)
        sleep(0.5)
        gpio.output(puerta,gpio.LOW)
    
    # Captura la imagen de ESP32-CAM
captured_image_path = capture_image()
    
if captured_image_path:
    #Llamamos la funcion para realizar la comparacion
    compare_faces(captured_image_path)