import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='headers_logs', exchange_type='headers')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#  The “x-match” property can have two different values: “any” or “all”,where “all” is the default value. A value of “all” means all header pairs (key, value) must match, while value of “any” means at least one of the header pairs must match.

args = {'x-match':'all','role':'ML_engineer'}

channel.queue_bind(exchange='headers_logs', queue=queue_name, arguments=args)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] message: {body}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
