
import asyncio

import pika


async def listener():
    global resultado
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='salon')
    channel.queue_declare(queue='habitacion')
    channel.queue_declare(queue='cocina')
    

    def callback_cocina(ch, method, properties, body):
        print(" [x] Received cocina %r" % body)
        with open("zcocina.txt","w") as f:
            f.write((body).decode("utf-8") )

    def callback_habitacion(ch, method, properties, body):
        print(" [x] Received habitacion %r" % body)
        with open("zhabitacion.txt","w") as f:
            f.write((body).decode("utf-8") )

    def callback_salon(ch, method, properties, body):
        print(" [x] Received salon %r" % body)
        with open("zsalon.txt","w") as f:
            f.write((body).decode("utf-8") ) 

    
    channel.basic_consume(queue='habitacion', on_message_callback=callback_habitacion, auto_ack=True)
    channel.basic_consume(queue='cocina', on_message_callback=callback_cocina, auto_ack=True)
    channel.basic_consume(queue='salon', on_message_callback=callback_salon, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+Cc')
    channel.start_consuming()

loop=asyncio.get_event_loop()
loop.run_until_complete(listener())