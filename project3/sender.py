import pika


# Connect to rabbitmq server
conn = pika.BlockingConnection(pika.ConnectionParameters(
    host = 'localhost'
))


# Create Channel
ch = conn.channel()


# Create Queue and Set name
ch.queue_declare(queue= 'q1', durable=True)


# Send message
message = 'this is testing message'
ch.basic_publish(
    exchange='', 
    routing_key='q1', 
    body= message ,
    properties=pika.BasicProperties(
        delivery_mode = 2,
        headers = {
            'name' : 'charlie',
        }
    ),
)


# Test send in terminal
print('Message Sent !')

# Close Connection
conn.close()

