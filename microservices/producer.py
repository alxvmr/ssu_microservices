from flask import Flask, request, jsonify
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.model import create_tables, OutboxMessage, Session

app = Flask(__name__)

# create_tables() # is used once to create the database

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json.get('message')
    
    # save the message to Outbox
    session = Session()
    outbox_message = OutboxMessage(message=message)
    session.add(outbox_message)
    session.commit()
    session.close()
    
    return jsonify({"status": "Message saved to Outbox", "message": message})

if __name__ == '__main__':
    app.run(port=5001)