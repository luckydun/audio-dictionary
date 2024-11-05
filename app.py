# app.py
import sys
print(sys.executable)
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS  # Import flask_cors
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Your routes and application logic here


DICTIONARY_API_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/word/<word>', methods=['GET'])
def get_word_info(word):
    try:
        response = requests.get(f'{DICTIONARY_API_URL}{word}')
        data = response.json()[0]
        info = {
            'definition': data['meanings'][0]['definitions'][0]['definition'],
            'pronunciation': data['phonetic'],
            'example': data['meanings'][0]['definitions'][0].get('example', 'No example available'),
        }
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)