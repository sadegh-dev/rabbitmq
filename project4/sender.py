import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
    )
)

ch = conn.channel()

ch.exchange_declare(
    exchange = 'fan_logs' , 
    exchange_type = 'fanout'
)

the_message = 'this is Testing fanout exchange !'

ch.basic_publish(
    exchange = 'fan_logs' , 
    routing_key = '' , 
    body = the_message 
)

print('Sent message !')

conn.close()
