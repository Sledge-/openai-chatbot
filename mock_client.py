import socketio
import time

# Standard Python client based on WebSocket transport
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected to the chat server!")

@sio.event
def disconnect():
    print("I'm disconnected from the chat server!")

# Connect to the Flask Socket.IO server
sio.connect('http://127.0.0.1:5151')

# Sending 10 messages with a delay
for i in range(1, 11):
    sio.emit('send_message', {'message': f'Message {i}'})
    print(f'Sent message {i}')
    time.sleep(1)  # Wait for a second before sending the next message

# Disconnect from the server
sio.disconnect()
