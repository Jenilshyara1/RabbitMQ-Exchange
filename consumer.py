import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(f" [x] Received '{body}'")
    ch.basic_ack(delivery_tag = method.delivery_tag) # to make sure a message is never lost

channel.basic_consume(queue='hello',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()