import pika
import time
from model import OutboxMessage, Session

def send_outbox_messages():
    while True:
        session = Session()
        messages = session.query(OutboxMessage).all()
        
        for message in messages:
            try:
                # sending a message to RabbitMQ
                connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                channel = connection.channel()
                channel.queue_declare(queue='service_b_queue')
                channel.basic_publish(exchange='', routing_key='service_b_queue', body=message.message)
                connection.close()
                
                # deleting a message from Outbox after successful sending
                session.delete(message)
                session.commit()
                print(f"Sent message: {message.message} and removed from Outbox")
            except Exception as e:
                print(f"Failed to send message: {message.message}, error: {e}")
        
        session.close()
        time.sleep(5)

if __name__ == '__main__':
    send_outbox_messages()