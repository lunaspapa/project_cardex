# Imports
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

# Initialize
app = Flask(__name__)
CORS(app)

# Simple home placeholder route
@app.route('/')
def home():
  return jsonify({"message": "Welcome to the Pokemon Card API Backend!"})
# Working

# Route for Pokemon API Call
@app.route('/pokemon', methods=['GET'])
def get_pokemon():
  # Fetching Pokemon from Generation I
  gen_i_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
  response = requests.get(gen_i_url)
  data = response.json()
  return jsonify(data)
# Working

if __name__ == "__main__":
  app.run(debug=True)
