import pika

conn = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost'
    )
)

ch = conn.channel()

ch.exchange_declare(
    exchange='topic_logs', 
    exchange_type='topic'
)

result = ch.queue_declare(
    queue='', 
    exclusive=True
)

qname = result.method.queue

# binding key ##########
binding_key = 'info.#'

ch.queue_bind(
    exchange='topic_logs', 
    queue=qname, 
    routing_key=binding_key
)

print('Wating for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f'info level : {body}')
    print(f'details : {method.routing_key}')
    print('******************')


ch.basic_consume(
    queue=qname, 
    on_message_callback=callback, 
    auto_ack= True
)

ch.start_consuming()
