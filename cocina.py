#Sensor apertura ventanas
#Luces

from pyfiglet import Figlet
import sys,random
import asyncio, datetime

import pika
def func(msg: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='cocina')

    channel.basic_publish(exchange='', routing_key='cocina', body=str(msg))
    print(f" [x] Sent {msg}")
    connection.close()

global luces, ventana , luces_titulo, sensor_ventana_titulo
luces=0
ventana=1

custom_fig = Figlet(font='digital')



sensor_ventana_titulo="""
███████╗       ██╗   ██╗███████╗███╗   ██╗████████╗ █████╗ ███╗   ██╗ █████╗ 
██╔════╝       ██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗
███████╗       ██║   ██║█████╗  ██╔██╗ ██║   ██║   ███████║██╔██╗ ██║███████║
╚════██║       ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║╚██╗██║██╔══██║
███████║██╗     ╚████╔╝ ███████╗██║ ╚████║   ██║   ██║  ██║██║ ╚████║██║  ██║
╚══════╝╚═╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""
luces_titulo="""
██╗     ██╗   ██╗ ██████╗███████╗███████╗
██║     ██║   ██║██╔════╝██╔════╝██╔════╝
██║     ██║   ██║██║     █████╗  ███████╗
██║     ██║   ██║██║     ██╔══╝  ╚════██║
███████╗╚██████╔╝╚██████╗███████╗███████║
╚══════╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝
"""                          
opciones="""Presione ENTER  y despues la opcion
            1. Prender o Apargar Luces
            2. Simular sensor de ventana
            q. para salir
"""



async def async_input(prompt):
    print(prompt, end='', flush=True)
    return (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()

async def mostrar():
    
    global luces, ventana , luces_titulo, sensor_ventana_titulo
    while True:
        await asyncio.sleep(0.2)
        

        
        luces_text=f'Las luces estan {"ON" if luces == 1 else "OFF"}'
        lu=custom_fig.renderText(luces_text)
        sensor_ventana_text=f'Sensor Ventana {"ON" if ventana == 1 else "OFF"}'
        ve=custom_fig.renderText(sensor_ventana_text)
        
        print(luces_titulo + lu ,sensor_ventana_titulo + ve)
        print(datetime.datetime.now())

async def runn():
    global ventana, luces
    loop.create_task(mostrar())
    while True:
        
        
        
        
        input(opciones)
        msg = await async_input('Enter a command: ')
        if msg == '1':
            print('luces')
            luces=0 if luces == 1 else 1
        elif msg == '2':
            print('ventana')
            ventana=0 if ventana == 1 else 1
        package={"cocina_luces":luces,"cocina_ventana":ventana}
        func(package)


        if msg == 'q':
            return
        await asyncio.sleep(3)
         

loop = asyncio.get_event_loop()
loop.run_until_complete(runn())