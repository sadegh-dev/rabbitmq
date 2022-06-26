import pika
import time

# Connection to rabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters(
    host = 'localhost'
))


# Create channel
ch = conn.channel()


# Create Queue and Set name
ch.queue_declare(queue='q1', durable=True)




# Receive message
def callback(ch, method, properties, body):
    print(f"Recive [{body}]")
    print(properties.headers)
    print(method)
    print(method.delivery_tag)
    time.sleep(5)
    print('Done.')
    ch.basic_ack(delivery_tag=method.delivery_tag)

ch.basic_qos(prefetch_count = 1)

ch.basic_consume(queue='q1', on_message_callback = callback)




print('Wating for message, to exit press ctl+c')

ch.start_consuming()