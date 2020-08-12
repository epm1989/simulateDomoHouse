#Boton inalambrico
#Persinanas
#Luces
from pyfiglet import Figlet
import sys,random
import asyncio, datetime
custom_fig = Figlet(font='digital')

import pika
def func(msg: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='habitacion')

    channel.basic_publish(exchange='', routing_key='habitacion', body=str(msg))
    print(f" [x] Sent {msg}")
    connection.close()

global persiana, boton, luces, boton_titulo , persianas_titulo , luces_titulo
persiana=1
boton=1
luces=1


boton_titulo ="""
██████╗  ██████╗ ████████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗████╗  ██║
██████╔╝██║   ██║   ██║   ██║   ██║██╔██╗ ██║
██╔══██╗██║   ██║   ██║   ██║   ██║██║╚██╗██║
██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║ ╚████║
╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
"""
persianas_titulo="""
██████╗ ███████╗██████╗ ███████╗██╗ █████╗ ███╗   ██╗ █████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗  ██║██╔══██╗██╔════╝
██████╔╝█████╗  ██████╔╝███████╗██║███████║██╔██╗ ██║███████║███████╗
██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║██╔══██║██║╚██╗██║██╔══██║╚════██║
██║     ███████╗██║  ██║███████║██║██║  ██║██║ ╚████║██║  ██║███████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
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
            1. Prender o Apagar Boton
            2. Subit o Bajar Persainas
            3. Prender o Apagar Luces
            q. para salir
"""





async def async_input(prompt):
    print(prompt, end='', flush=True)
    return (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()

async def mostrar():
    
    global persiana, boton, luces, boton_titulo , persianas_titulo , luces_titulo
    while True:
        await asyncio.sleep(0.2)
        

        
        luces_text=f'Las luces estan {"ON" if luces == 1 else "OFF"}'
        lu=custom_fig.renderText(luces_text)
        boton_text=f'Sensor Ventana {"ON" if boton == 1 else "OFF"}'
        bo=custom_fig.renderText(boton_text)
        persiana_texto= f'Persianas {"UP" if persiana == 1 else "DOWN"}'
        pe=custom_fig.renderText(persiana_texto)
        
        print(boton_titulo + bo,persianas_titulo + pe, luces_titulo + lu )
        print(datetime.datetime.now())

async def runn():
    global persiana, boton, luces, boton_titulo , persianas_titulo , luces_titulo
    loop.create_task(mostrar())
    while True:
        
        
        
        
        input(opciones)
        msg = await async_input('Enter a command: ')
        if msg == '1':
            print('boton')
            boton=0 if boton == 1 else 1
        elif msg == '2':
            print('persiana')
            persiana=0 if persiana == 1 else 1
        elif msg == '3':
            print('luces')
            luces=0 if luces == 1 else 1
        package={"habitacion_boton":boton,"habitacion_persiana":persiana,"habitacion_luces":luces}
        func(package)


        if msg == 'q':
            return
        await asyncio.sleep(3)
         

loop = asyncio.get_event_loop()
loop.run_until_complete(runn())