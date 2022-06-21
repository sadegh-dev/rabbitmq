import pika


# Connection to rabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters(
    host = 'localhost'
))


# Create channel
ch2 = conn.channel()


# Create Queue and Set name
ch2.queue_declare(queue='street1')


# Receive message
def callback(ch, method, properties, body):
    print(f"Recive[{body}]")


ch2.basic_consume(
    queue = 'street1' ,
    on_message_callback = callback , 
    auto_ack = True
)

print('Wating for message, to exit press ctl+c')

ch2.start_consuming()