from select import EPOLLEXCLUSIVE
import pika
import uuid


class Sender:
    def __init__(self):
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost'
            )
        )
        self.ch = self.conn.channel()
        result = self.ch.queue_declare(
            queue='',
            exclusive=True
        )
        self.qname = result.method.queue
        self.ch.basic_consume(
            queue= self.qname ,
            on_message_callback = self.my_response,
            auto_ack = True
        )


    def my_response(self, ch, method, proper, body):
        if self.corr_id == proper.correlation_id :
            self.response = body


    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.ch.basic_publish(
            exchange='' ,
            routing_key = 'rpc_queue' ,
            body = str(n) ,
            properties = pika.BasicProperties(
                reply_to = self.qname ,
                correlation_id = self.corr_id ,
            )
        )
        while self.response is None :
            self.conn.process_data_events()

        return self.response
        # return int(self.response)



send = Sender()

response = send.call(22)

print(response)
