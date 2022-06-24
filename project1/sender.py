import pika
import time


# Connect to rabbitmq server
conn = pika.BlockingConnection(pika.ConnectionParameters(
    host = 'localhost'
))


# Create Channel
ch1 = conn.channel()


# Create Queue and Set name
ch1.queue_declare(queue= 'street1')


# Send message
ch1.basic_publish(exchange='', routing_key='street1', body=time.ctime())


# Test send in terminal
print('Message Sent !')

# Close Connection
conn.close()

