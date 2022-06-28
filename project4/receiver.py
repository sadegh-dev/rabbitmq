import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
    )
)

ch = conn.channel()

ch.exchange_declare(
    exchange = 'fan_logs', 
    exchange_type = 'fanout'
)

### Way1 ###

result = ch.queue_declare(
    queue = '' , 
    exclusive = True
)

qname = result.method.queue

######## End of Way1 #####


### Way2 ###
"""
ch.queue_declare(
    queue = 'aa'
)
qname = 'aa'
"""
######## End of Way2 #####


ch.queue_bind(
    exchange = 'fan_logs', 
    queue = qname
)

print('Wating ...!')

def callback(ch, method, properties, body):
    print(f'received {body}')
    print(f'qname is {qname}')
    print('--------------------')


ch.basic_consume(
    queue = qname , 
    on_message_callback = callback , 
    auto_ack = True
)

ch.start_consuming()

