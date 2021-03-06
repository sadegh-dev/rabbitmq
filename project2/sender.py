import pika

# Connect to rabbitmq server
conn = pika.BlockingConnection(pika.ConnectionParameters(
    host = 'localhost'
))


# Create 2 Channels
ch = conn.channel()


# Create Queue and Set name
ch.queue_declare(queue= 'street_odd')
ch.queue_declare(queue= 'street_even')



# Send message
for x in range(10) :
    f_send = f'send number {x}'
    if x % 2 == 0 :   
        ch.basic_publish(exchange='', routing_key='street_even', body= f_send)
    else :
        ch.basic_publish(exchange='', routing_key='street_odd', body= f_send)


# Test send in terminal
print('Message Sent !')

# Close Connection
conn.close()
