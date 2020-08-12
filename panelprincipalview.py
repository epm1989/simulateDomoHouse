from pyfiglet import Figlet
from time import sleep
import asyncio,datetime,json
import ast

global cocina, salon , habitacion, resultado
custom_fig = Figlet(font='mini')
custom_fig1 = Figlet(font='digital')







async def mostrar():
    print("mostrar")
    global cocina, salon , habitacion, resultado
    resultado={}
    while True:
        print("mostrar")
        await asyncio.sleep(2)
        #sleep(1)
        print("mostrar")
        with open("zcocina.txt","r") as fc:
            lectura= fc.read()
            resultado["cocina"]=ast.literal_eval(lectura)

        
        with open("zhabitacion.txt","r") as fh:
            lectura = fh.read()
            resultado["habitacion"]=ast.literal_eval(lectura)
            
        
        with open("zsalon.txt","r") as fs:
            lectura = fs.read()
            print(type(lectura))
            resultado["salon"]=ast.literal_eval(lectura)
        
        print(resultado)
    
        salon_text="--SALON--"
        sa=custom_fig.renderText(salon_text)

        sa_lu=custom_fig1.renderText(f"Luces {'ON' if resultado['salon']['salon_luces'] == 1 else 'OFF'}")
        sa_mo=custom_fig1.renderText(f"Movimiento {'ON' if resultado['salon']['salon_mov'] == 1 else 'OFF'}")
        sa_te=custom_fig1.renderText(f"Termostato {'ON' if resultado['salon']['salon_termo'] == 1 else 'OFF'}  la temp es: {resultado['salon']['salon_temp']}")

        habitacion_text="--HABITACION--"
        ha=custom_fig.renderText(habitacion_text)

        ha_lu=custom_fig1.renderText(f"Luces {'ON' if resultado['habitacion']['habitacion_luces'] == 1 else 'OFF'}")
        ha_pe=custom_fig1.renderText(f"Persianas {'ON' if resultado['habitacion']['habitacion_persiana'] == 1 else 'OFF'}")
        ha_bo=custom_fig1.renderText(f"Boton {'ON' if resultado['habitacion']['habitacion_boton'] == 1 else 'OFF'}")

        cocina_text="--COCINA--"
        co=custom_fig.renderText(cocina_text)

        
        co_lu=custom_fig1.renderText(f"Luces {'ON' if resultado['cocina']['cocina_luces'] == 1 else 'OFF'}")
        co_ve=custom_fig1.renderText(f"Ventanas {'ON' if resultado['cocina']['cocina_ventana'] == 1 else 'OFF'}")
        
        print(sa+sa_lu+sa_mo+sa_te,ha + ha_lu + ha_bo + ha_pe,co+co_lu + co_ve)
        print(resultado)
        print(datetime.datetime.now())
    
loop=asyncio.get_event_loop()
loop.run_until_complete(mostrar())