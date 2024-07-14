import nltk
from nltk.chat.util import Chat, reflections

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

def chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()
