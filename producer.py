from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json.get('message')
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='service_b_queue')
    channel.basic_publish(exchange='', routing_key='service_b_queue', body=message)
    
    connection.close()
    return jsonify({"status": "Message sent", "message": message})

if __name__ == '__main__':
    app.run(port=5001)