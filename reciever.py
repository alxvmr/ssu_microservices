import pika

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Service C received event: {message}")

def start_service_c():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='service_c_queue')
    channel.basic_consume(queue='service_c_queue', on_message_callback=callback, auto_ack=True)
    
    print('Service C is waiting for events. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_service_c()