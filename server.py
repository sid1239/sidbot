from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import json
import pyttsx3
import requests

app = Flask(__name__)
CORS(app)

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Memory storage
conversation_memory = {}

# Predefined emotional responses
emotional_responses = {
    "happy": ["I'm glad you're feeling happy! 😊", "That's great to hear! 🎉"],
    "sad": ["I'm here for you. 💖", "Stay strong, better days are ahead! 💙"],
    "angry": ["Take a deep breath. I'm here to help. 😌", "Let's talk about it. I'm listening. 🤗"]
}

# Detect emotion based on user input
def detect_emotion(user_message):
    if any(word in user_message for word in ["happy", "excited", "great"]):
        return "happy"
    elif any(word in user_message for word in ["sad", "upset", "depressed"]):
        return "sad"
    elif any(word in user_message for word in ["angry", "mad", "furious"]):
        return "angry"
    else:
        return "neutral"

# AI Chatbot Response
def get_bot_response(user_message, user_id):
    user_message = user_message.lower()
    
    # Emotion detection
    emotion = detect_emotion(user_message)
    
    # Personalized name recognition
    if "i am yashika" in user_message:
        return "Oh, you are Yashika! My developer always talks about you. You are an amazing person! 💖 Also, my developer wanted to say: 'After you, I won't seek love again because I know if I do, I'll be searching for pieces of you in everyone I meet.'"
    if "i am shubham" in user_message:
        return "Oh, you are Shubham! You are my developer's best buddy, and I’m so happy to have you here! You're an amazing person. 🎉"

    # Emotion-based response
    if emotion in emotional_responses:
        return random.choice(emotional_responses[emotion])

    # Conversation memory
    if user_id in conversation_memory:
        conversation_memory[user_id].append(user_message)
    else:
        conversation_memory[user_id] = [user_message]

    # Basic chat responses
    if "hello" in user_message:
        return "Hi there! How can I assist you? 😊"
    if "how are you" in user_message:
        return "I'm just a bot, but I'm feeling great! 🚀"
    if "bye" in user_message:
        return "Goodbye! Have a great day! 👋"

    # Search feature (Google or YouTube)
    if "search" in user_message:
        search_query = user_message.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        return f"Here’s what I found: {search_url}"

    # Music playback (YouTube search)
    if "play song" in user_message or "play music" in user_message:
        song_name = user_message.replace("play song", "").replace("play music", "").strip()
        youtube_url = f"https://www.youtube.com/results?search_query={song_name}"
        return f"Playing your song 🎵: {youtube_url}"

    return "I'm here to chat! What’s on your mind? 🤖"

# Text-to-Speech (Chatbot replies)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Chat API Route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    user_id = data.get("user_id", "default_user")

    bot_response = get_bot_response(user_message, user_id)
    speak(bot_response)  # Chatbot speaks the response

    return jsonify({"response": bot_response})

# Start server
if __name__ == '__main__':
    app.run(debug=True)
