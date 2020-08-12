#Termostato
#Sensor Movimeinto
#Luces
from pyfiglet import Figlet
import sys,random
import asyncio, datetime

import pika
def func(msg: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='salon')

    channel.basic_publish(exchange='', routing_key='salon', body=str(msg))
    print(f" [x] Sent {msg}")
    connection.close()

custom_fig = Figlet(font='digital')

global luces, movimiento, temp, ter , luces_titulo, termostato_titulo, sensor_movimiento_titulo
luces=0
movimiento=1
temp=26
ter=1



termostato_titulo="""
████████╗███████╗██████╗ ███╗   ███╗ ██████╗ ███████╗████████╗ █████╗ ████████╗ ██████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║███████╗   ██║   ███████║   ██║   ██║   ██║
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║╚════██║   ██║   ██╔══██║   ██║   ██║   ██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝███████║   ██║   ██║  ██║   ██║   ╚██████╔╝
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""                                                                                        

sensor_movimiento_titulo="""
███████╗       ███╗   ███╗ ██████╗ ██╗   ██╗██╗███╗   ███╗██╗███████╗███╗   ██╗████████╗ ██████╗ 
██╔════╝       ████╗ ████║██╔═══██╗██║   ██║██║████╗ ████║██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗
███████╗       ██╔████╔██║██║   ██║██║   ██║██║██╔████╔██║██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║
╚════██║       ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║██║██╔══╝  ██║╚██╗██║   ██║   ██║   ██║
███████║██╗    ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║██║███████╗██║ ╚████║   ██║   ╚██████╔╝
╚══════╝╚═╝    ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ 
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
            1. Prender o Apagar Termostato
            2. Prender o Apargar Luces
            3. Simular detector de movimiento
            q. para salir
"""

async def async_input(prompt):
    print(prompt, end='', flush=True)
    return (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()

async def mostrar():
    print('ddd')
    global temp,ter, luces_titulo
    while True:
        await asyncio.sleep(0.2)
        if ter == 1:
            a=temp-1
            b=temp+2
        else:
            a=temp-2
            b=temp+1

        temp=random.randint(a,b)
        luces_text=f'Las luces estan {"ON" if luces == 1 else "OFF"}'
        lu=custom_fig.renderText(luces_text)
        sensor_movimiento_text=f'Sensor Movieminto {"ON" if movimiento == 1 else "OFF"}'
        mo=custom_fig.renderText(sensor_movimiento_text)
        termostato_texto= 'La temperatura es {1}, Termostato {0}'.format("ON" if ter == 1 else "OFF",temp)
        te=custom_fig.renderText(termostato_texto)
        print(termostato_titulo + te,luces_titulo + lu ,sensor_movimiento_titulo + mo)
        print(datetime.datetime.now())

async def runn():
    global ter, luces, movimiento
    loop.create_task(mostrar())
    while True:
        
        
        
        
        input(opciones)
        msg = await async_input('Enter a command: ')
        if msg == '1':
            print('termos')
            ter=0 if ter == 1 else 1
        elif msg == '2':
            print('luces')
            luces=0 if luces == 1 else 1
        elif msg == "3":
            print("movimiento")
            movimiento=0 if movimiento == 1 else 1
        package={"salon_termo":ter,"salon_luces":luces,"salon_mov":movimiento,"salon_temp":temp}
        func(package)

        if msg == 'q':
            return
        await asyncio.sleep(3)
         

loop = asyncio.get_event_loop()
loop.run_until_complete(runn())
