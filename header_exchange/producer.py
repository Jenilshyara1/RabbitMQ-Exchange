import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='headers_logs', exchange_type='headers')

headers = {'role':'ML_engineer'}
message = f'Hello {headers["role"]}'

channel.basic_publish(exchange='headers_logs',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(
                          headers=headers  # add headers to the message
                      ))
print(f" [x] Sent '{message}'")
connection.close()
