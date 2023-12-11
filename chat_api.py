# app.py
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from conversation_manager import ConversationManager

context_window = 10000
conversation_manager = ConversationManager(context_window)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}) # Adjust origins as needed
socketio = SocketIO(app, cors_allowed_origins="http://localhost:8080") # Allow all origins for SocketIO

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('send_message')
def handle_send_message_event(data):
    # Here you can add your concatenate_strings function and other logic
    message = data['message']
    print(f"Received message: {message}")
    response = conversation_manager.submit_message(message)
    print(f"response: {response}")
    emit('receive_message', response, broadcast=True)

@socketio.on('request_summary')
def handle_summary_request():
    # Generate the conversation summary
    summary = conversation_manager.get_summary()

    # Send the summary back to the client
    emit('summary_response', summary)

if __name__ == '__main__':
    socketio.run(app, port=5151, debug=True) 
