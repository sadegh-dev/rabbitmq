import pika


# Connect to RaabitMQ

conn = pika.BlockingConnection(
	pika.ConnectionParameters(
		host='localhost'
	)
)

ch  = conn.channel()


# Create Exchange

ch.exchange_declare(
	exchange='direct_logs', 
	exchange_type='direct'
)

messages = {
	'info' : 'info about line ' ,
	'error' : 'error about line ' ,
	'warning' : 'warning about line '
}

for tt, mm in messages.items():
	ch.basic_publish(
		exchange='direct_logs', 
		routing_key=tt, 
		body = mm
	)
	print(f'sent message {tt} !')
conn.close()


