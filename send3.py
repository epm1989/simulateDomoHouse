#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='cocina')

channel.basic_publish(exchange='', routing_key='cocina', body='Hello World3!')
print(" [x] Sent 'Hello World!'")
connection.close()
