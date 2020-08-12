#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='salon')
channel.queue_declare(queue='habitacion')
channel.queue_declare(queue='cocina')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='salon', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='habitacion', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='cocina', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
