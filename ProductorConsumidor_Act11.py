import keyboard
import threading
import time
import random
import os

CAPACIDAD = 25
buffer = [0] * CAPACIDAD
indice_productor = 0
indice_consumidor = 0

sem_buffer = threading.Semaphore(1)

def stop_app():
    print("\nFinaliza el programa")
    os._exit(0)

def productor():
    global buffer, indice_productor
    while True:
        tiempo_dormido = random.randint(1, 5)
        print(f"\nProductor dormido por {tiempo_dormido} segundos")
        time.sleep(tiempo_dormido)
        funcion_ejecutar = random.choice([productor, consumidor])
        if funcion_ejecutar == productor:
            sem_buffer.acquire()
            if buffer[indice_productor] == 0:
                print("\nProductor entro")
                cantidad_elementos = random.randint(1, 5)
                print("\nElementos creados:", cantidad_elementos)
                for i in range(cantidad_elementos):
                    buffer[indice_productor] = 1
                    indice_productor = (indice_productor + 1) % CAPACIDAD
                    if buffer[indice_productor] != 0:
                        break
            print("Buffer", buffer)
            sem_buffer.release()


def consumidor():
    global buffer, indice_consumidor
    while True:
        tiempo_dormido = random.randint(1, 5)
        print(f"\nConsumidor dormido por {tiempo_dormido} segundos")
        time.sleep(tiempo_dormido)
        funcion_ejecutar = random.choice([productor, consumidor])
        if funcion_ejecutar == consumidor:
            sem_buffer.acquire()
            if buffer[indice_consumidor] != 0:
                print("\nConsumidor entro")
                cantidad_elementos = random.randint(1, 5)
                print("\nElementos consumidos:", cantidad_elementos)
                for i in range(cantidad_elementos):
                    if buffer[indice_consumidor] == 0:
                        break
                    buffer[indice_consumidor] = 0
                    indice_consumidor = (indice_consumidor + 1) % CAPACIDAD
                    if buffer[indice_consumidor] == 0:
                        break
            print("Buffer", buffer)
            sem_buffer.release()

#hilos
hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)
hilo_productor.start()
hilo_consumidor.start()

keyboard.add_hotkey('escape', stop_app)
