
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch  = conn.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

messages = {
	'info.weblog.signup' : 'signup new user' ,
    'info.shop.signout' : 'sign out user' ,
    'error.shop.admin' : 'error admin in shop' ,
}

for tt, mm in messages.items():
	ch.basic_publish(exchange='topic_logs', routing_key=tt , body = mm)
	print(f'sent messages {tt} !')
conn.close()

