import pika
import time
import json

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Service B received: {message}")
    
    # Обработка сообщения
    time.sleep(1)
    
    # Отправка события в Service C
    send_event_to_service_c(message)

def send_event_to_service_c(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='service_c_queue')
    channel.basic_publish(exchange='', routing_key='service_c_queue', body=message)
    
    connection.close()

def start_service_b():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='service_b_queue')
    channel.basic_consume(queue='service_b_queue', on_message_callback=callback, auto_ack=True)
    
    print('Service B is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_service_b()