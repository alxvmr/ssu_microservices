from flask import Flask, request, jsonify
from db.model import create_tables, OutboxMessage, Session

app = Flask(__name__)

# create_tables() # используется 1 раз для создания БД

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json.get('message')
    
    # Сохраняем сообщение в Outbox
    session = Session()
    outbox_message = OutboxMessage(message=message)
    session.add(outbox_message)
    session.commit()
    session.close()
    
    return jsonify({"status": "Message saved to Outbox", "message": message})

if __name__ == '__main__':
    app.run(port=5001)