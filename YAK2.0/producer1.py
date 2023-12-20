import pika
from pika.exchange_type import ExchangeType
import sys
from broker import *
topic=sys.argv[1]
key=sys.argv[2]
#val=sys.argv[2]
msg="Have a nice day"
check(topic,msg,key)

connection_parameters=pika.ConnectionParameters('localhost')

connection=pika.BlockingConnection(connection_parameters)

channel = connection.channel()#creates a channel 
#create connection for the channel

#declare queue
channel.exchange_declare(exchange='mytopic',exchange_type=ExchangeType.topic)

#define the message u would like to send
#msg="Have a nice day"
channel.basic_publish(exchange='mytopic',routing_key=topic,body=msg)

print(f"sent message:{msg}")

connection.close()