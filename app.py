import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify, send_from_directory

# Download necessary NLTK data
nltk.download('punkt')

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name?', ["I'm a simple chatbot.", "You can call me ChatBot."]),
    (r'how are you?', ["I'm doing well, thanks!", "I'm fine, how about you?"]),
    (r'what can you do?', ["I can chat with you!", "I can answer simple questions."]),
    (r'bye|goodbye', ["Goodbye!", "See you later!", "Bye!"]),
    (r'.*', ["I'm not sure how to respond to that.", "Can you rephrase that?", "Let's talk about something else."])
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot.respond(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)