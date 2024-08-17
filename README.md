
# Sistema de control de acceso con reconocimiento de tarjeta

### Solución propuesta

La seguridad y la facilidad para la recolección de datos ya no son un simple sueño o un privilegio, actualmente es una necesidad y la queremos cubrir con este proyecto limitando la entrada a personal no autorizado en áreas restringidas con el control de acceso con tarjeta en un sistema de seguridad.
Implementándolo en empresas y edificios.
De modo que al utilizar una tarjeta de radiofrecuencia y un lector de esta misma se obtendrá el acceso a dicho establecimiento ademas de registrar las entradas y salidas en una base de datos.

### Objetivos específicos
- Prevenir el acceso no autorizado a instalaciones o áreas restringidas mediante la verificación de identidad a través de tarjetas personalizadas.

- Registrar y rastrear los movimientos de empleados, visitantes o residentes para fines de seguridad y seguimiento.

- Facilitar la gestión de horarios de trabajo al permitir o denegar el acceso según el turno o la autorización.

- Proporcionar una solución conveniente y rápida para el acceso, evitando la necesidad de llaves.


### Software
- Raspberry pi OS

- NODE-RED

- Arduino IDE

### Librerías para Raspberry pi OS
- import os

- import sys

- import requests

- from datetime import datetime

- import paho.mqtt.client as mqtt

- import json

- import RPi.GPIO as gpio

- from time import sleep

- import paho.mqtt.client as mqtt

### Control de acceso con RFID
**Introducción**

Se muestran los recursos e instrucciones necesarios para la creación de un sistema de control de acceso de personal mediante un lector RFID.  Dicho acceso será representado por un par de leds, los cuales simularán la autorización o negación del acceso: cuando el led rojo se encienda significa que el acceso se denegó y cuando el led verde se encienda, significa que el acceso se autorizó. 

**Objetivo**

Accionar los pines GPIO de la Raspberry pi 4 mediante la lectura de la tarjeta RFID usando el lector RFID-RC522 para indicar si se concede el acceso o se rechaza el acceso.

**Materiales**
- Sensor RFID MFRC522 RF IC

- GPIO Extension Board 

- Protoboard

- LEDS

- Jumpers

- Resistencias de 220 Ohms

- Tarjetas RFID

- Raspberry Pi 4

**Circuito sugerido**

[![Circuito-rpi-rfid.jpg](https://i.postimg.cc/tRcSyWqn/Circuito-rpi-rfid.jpg)](https://postimg.cc/7bgMnCTq)

### Registro de rostros con ESP-32 CAM

**Introducción**

Se muestran los recursos necesarios para la creación de un sistema de reconocimiento facial mediante un ESP32-CAM. Dicho reconocimiento facial detonará el comportamiento de un par de leds, los cuales simularán la apertura de una cerradura: cuando el led rojo se encienda significa que la puerta se encuentra cerrada, y cuando el led verde se encienda, significa que la puerta está abierta. 

**Objetivo** 

Capturar una imagen del usuario presente y mandarla ala base de datos para analizarla y determinar si tiene acceso o es rechazado.

**Materiales**

- ESP32-CAM

- Convertidor serie USB FTDI TTL FT232RL 

- Protoboard

- Jumpers

**Circuito sugerido**

[![Circuito-esp32-cam.jpg](https://i.postimg.cc/0Qz8MDLK/Circuito-esp32-cam.jpg)](https://postimg.cc/KkyXCkcm)

## Flows en NODE-RED
[![flow1.jpg](https://i.postimg.cc/ZRjvx8Rb/flow1.jpg)](https://postimg.cc/FddK9J38)

[![flow2.jpg](https://i.postimg.cc/yxkxh2tj/flow2.jpg)](https://postimg.cc/ctGd0kst)

## Base de datos
[![Base-de-datos.jpg](https://i.postimg.cc/26vrzmsP/Base-de-datos.jpg)](https://postimg.cc/KkZdfXvN)

## Dashboard de NODE-RED

[![dashboard.jpg](https://i.postimg.cc/3J97rtqJ/dashboard.jpg)](https://postimg.cc/BX8RMBsd)

## Resultados de elaboración
[![resultados.jpg](https://i.postimg.cc/C5PvXnvY/resultados.jpg)](https://postimg.cc/JHXcB0Vd)

[![resultados2.jpg](https://i.postimg.cc/MKfbqLH1/resultados2.jpg)](https://postimg.cc/7fDTNmgL)

## Resultados esperados
Con este proyecto esperamos crear un sistema de seguridad de dos niveles por lo que primero debe de haberse registrado el rostro y su respectiva tarjeta RFID de cada usuario de confianza ya que solo aprobando estos dos niveles se le conceerá el acceso, por lo que si pasa solo un nivel no es posible otorgarle el acceso.

## Conclusiones 
Este proyecto tiene un enfoque para mejorar la seguridad tanto a la hora de entrada y salida además de registrar estos eventos en una base de datos en la nube para poder monitorearla desde el puesto asignado a la supervisión de este sistema y alertar sobre posibles intrusos que atenten contra la seguridad física y material dentro del área controlada.

## Materiales de referencia

- [Curso IOT Essental Developer](https://edu.codigoiot.com/course/view.php?id=1042)
- [Apertura de puerta con reconocimiento facial](https://edu.codigoiot.com/course/view.php?id=856)

- [Control de acceso vehicular](https://edu.codigoiot.com/mod/lesson/view.php?id=2089)

- [Servidor del internet de las cosas con NODE-RED](https://edu.codigoiot.com/course/view.php?id=997)

Este proyecto fue realizado en el marco del curso IoT Essentials Developer impartido por [Codigo IoT ](https://www.codigoiot.com/) y organizado por la [Asociación Mexicana del Internet de las Cosas](https://www.asociacioniot.org/).