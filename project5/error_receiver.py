import pika

conn = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost'
    )
)

ch = conn.channel()

ch.exchange_declare(
    exchange='direct_logs', 
    exchange_type='direct'
)

result = ch.queue_declare(
    queue='', 
    exclusive=True
)

qname = result.method.queue

level = 'error'

ch.queue_bind(
    exchange='direct_logs', 
    queue=qname, 
    routing_key=level
)

print("Wating for logs. To exit press CTRL+C")

def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(str(body)+'\n')
    print(f'{method.routing_key}', {body})

ch.basic_consume(
    queue=qname, 
    on_message_callback=callback, 
    auto_ack= True
)

ch.start_consuming()









