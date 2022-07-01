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
            pass






send = Sender()

