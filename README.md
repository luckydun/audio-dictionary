# Audio Dictionary 🎧📖

A **Flask-powered audio dictionary** with a simple web interface. Users can speak a word and get its definition, pronunciation, and example usage via the **Dictionary API**.

## Features
- **Voice Recognition**: Speak a word to search for its meaning.
- **Text-to-Speech**: Listen to the definition.
- **Backend with Flask**: Simple API integration.
- **CORS Enabled**: Cross-Origin Resource Sharing to handle frontend-backend requests.

## Technologies Used
- **Flask**: Python web framework for the backend.
- **JavaScript & HTML**: Frontend to capture voice input.
- **Dictionary API**: Fetches word definitions and usage examples.
- **Web Speech API**: Handles voice recognition and synthesis.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/luckydun/audio-dictionary.git

## After you have successfully cloned
install dependecies i.e

pip install flask flask-cors requests

## Then run the flask server
python app.py
