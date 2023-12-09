import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1]       # (name).(role).(experience)

args = routing_key.split(".")
message = f"Hello My name is {args[0]} , I am a {args[1]} and  i have {args[2]} years of experience"

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(f" [x] Sent {routing_key}:{message}")
connection.close()