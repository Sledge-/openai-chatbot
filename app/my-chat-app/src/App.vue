<template>
  <div id="app">
    <ul id="messages">
      <li v-for="message in messages" :key="message.id">{{ message.text }}</li>
    </ul>
    <input v-model="newMessage" type="text" placeholder="Type a message...">
    <button @click="sendMessage">Send</button>
  </div>
  <div id="app">
    <!-- ... existing elements ... -->
    <button @click="requestSummary">Get Conversation Summary</button>
  </div>
</template>

<script>
import io from 'socket.io-client';

export default {
  name: 'App',
  data() {
    return {
      socket: null,
      newMessage: '',
      messages: [],
    };
  },
  created() {
    this.socket = io('http://localhost:5151');

    this.socket.on('connect', () => {
      console.log('Connected to chat server');
    });

    this.socket.on('receive_message', (data) => {
      console.log(data)
      this.messages.push({ text: data, id: this.messages.length });
    });


    this.socket.on('summary_response', (summary) => {
      // Handle the summary here
      // For example, display it in an alert or add it to the messages array
      alert('Conversation Summary: ' + summary);
      this.messages.push({ text: summary, id: this.messages.length})

    });
  },
  methods: {
    sendMessage() {
      if(this.newMessage.trim() !== '') {
        this.messages.push({ text: this.newMessage, id: this.messages.length });
        this.socket.emit('send_message', { message: this.newMessage });
        console.log(this.newMessage);
        this.newMessage = '';
      }
    },
    requestSummary() {
      // Send a command to the server to request a conversation summary
      this.socket.emit('request_summary', );
    }
  },
};
</script>

<style>
#body {
  background-color: #636b59; /* Replace with your dark blue hex code */
  color: #fff; /* Replace with the color you want for the text */
  /* Add any other global styles here */
}

#app {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  border-radius: 5px;
  background-color: #0b1a24;
}

#messages {
  list-style-type: none;
  padding: 0;
  max-height: 300px;
  overflow-y: scroll;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
  background-color: #153c5f;
  color: #66b8cb;
}

#messages li {
  padding: 5px 10px;
  border-bottom: 1px solid #e0ca73;
}

#messages li:last-child {
  border-bottom: none;
}

input[type="text"] {
  width: 70%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-right: 10px;
}

button {
  padding: 10px 15px;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
