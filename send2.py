#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='habitacion')

channel.basic_publish(exchange='', routing_key='habitacion', body='Hello World2!')
print(" [x] Sent 'Hello World!'")
connection.close()
