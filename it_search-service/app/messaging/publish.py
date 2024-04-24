#!/usr/bin/env python
import pika, sys


# подключение
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# создание очереди - желательно всегда прописывать и в отправителе, и получателе
channel.queue_declare(queue='hello')

# отправка сообщения
# чтобы сообщение не удалялись при закрытии сервера, их нужно пометить как persistance в properties (не полная гарантия)
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = pika.DeliveryMode.Persistent
                      ))
print(f" [x] Sent {message}")

connection.close()