import pika
from pika.exchange_type import ExchangeType
import sys
from broker import *
topic=sys.argv[1]
val=sys.argv[2]


def on_message_received(ch,method,properties,body):
    if(val=="--from-beginning"):
        read_brok(topic)
    elif(val=="n"):
        print(f"first consumer 1:received message:{body}") 
   
connection_parameters=pika.ConnectionParameters('localhost')

connection=pika.BlockingConnection(connection_parameters)

channel = connection.channel()#creates a channel 

channel.exchange_declare(exchange='mytopic',exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='',exclusive=True)


channel.queue_bind(exchange='mytopic',queue=queue.method.queue,routing_key=topic)

channel.basic_consume(queue=queue.method.queue,auto_ack=True, on_message_callback=on_message_received)
print("Starting consuming")



channel.start_consuming()    