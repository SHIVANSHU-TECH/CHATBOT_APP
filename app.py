from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Get weather information from an external API
def get_weather():
    try:
        response = requests.get("https://api.weather.com/...")
        # Process the API response and extract relevant weather information
        weather_info = process_response(response)
        return weather_info
    except requests.RequestException:
        return "Sorry, unable to fetch weather information."

# Placeholder function to process API response
def process_response(response):
    # Implement your logic here to extract weather information from the response
    # Return the extracted information as a string
    return "Today's weather is sunny and warm."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('user_input')
    response = ""

    if user_input:
        if "name" in user_input.lower():
            response = "You can call me ChatBot. How can I assist you?"
        elif "joke" in user_input.lower():
            response = "Sure! Why don't scientists trust atoms? Because they make up everything!"
        elif "weather" in user_input.lower():
            response = get_weather()
        elif "bye" in user_input.lower():
            response = "Goodbye! Have a great day!"
        elif "help" in user_input.lower():
            response = "I'm here to assist you. How can I help you?"
        elif "time" in user_input.lower():
            response = "The current time is 2:30 PM."
        elif "news" in user_input.lower():
            response = "Here are the latest news headlines: ..."
        elif "how are you" in user_input.lower():
            response = "I'm doing well, thank you for asking!"
        elif "tell me a fact" in user_input.lower():
            response = "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
        elif "what is your favorite color" in user_input.lower():
            response = "As an AI, I don't have personal preferences, but I think all colors are beautiful!"
        elif "tell me a riddle" in user_input.lower():
            response = "I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I? Answer: A keyboard."
        elif "do you have any siblings" in user_input.lower():
            response = "As an AI, I don't have family or siblings in the traditional sense, but I have fellow AI counterparts."
        elif "what is your favourite food" in user_input.lower():
            response = "I don't have personal preferences when it comes to food, but I can assist you in finding recipes or restaurants!"

        else:
            response = "I'm sorry, I didn't understand. Can you please rephrase your query?"
    else:
        response = "Please provide some input."

    return jsonify({'bot_response': response}), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(port=5000)
