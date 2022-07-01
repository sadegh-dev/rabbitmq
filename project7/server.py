import queue
from statistics import correlation
import pika
import time

conn = pika.BlockingConnection(
    pika.ConnectionParameters(
        host = 'localhost'
    )
)
ch = conn.channel()
ch.queue_declare(queue='rpc_queue')


def callback(ch, method, proper, body):
    n = int(body)
    print('processing received data !')
    time.sleep(4)
    response = n+1
    ch.basic_publish(
        exchange='',
        routing_key = proper.reply_to ,
        body = str(response) ,
        properties = pika.BasicProperties(
            correlation_id = proper.correlation_id
        )
    )
    ch.basic_ack( delivery_tag = method.delivery_tag )


ch.basic_qos(prefetch_count = 1)
ch.basic_consume(
    queue='rpc_queue',
    on_message_callback = callback ,    
)
print('Wating for message !')

ch.start_consuming()
