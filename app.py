# Imports
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

# Get API key from .env
API_KEY = os.environ.get("TCG_API_KEY")

# Initialize
app = Flask(__name__)
CORS(app)

# é (Alt+0233) (For proper stylization of Pokémon)

# Simple home placeholder route
@app.route('/')
def home():
  return jsonify({"message": "Welcome to the Pokémon Card API Backend!"})
# Working

# Route for Pokémon API Call
@app.route('/pokemon', methods=['GET'])
def get_pokemon():
  # Fetching Pokémon from Generation I
  gen_i_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
  response = requests.get(gen_i_url)
  data = response.json()
  return jsonify(data)
# Working

# Route for calling TCG API on a Pokémon
@app.route('/cards/<pokemon_name>', methods=['GET'])
def get_cards(pokemon_name):
  tcgapi_url = f"https://api.pokemontcg.io/v2/cards?q=name:{pokemon_name}"
  # Headers for API
  headers = {"X-Api_Key": API_KEY}
  response = requests.get(tcgapi_url, headers=headers)
  data = response.json()
  return jsonify(data)
# Working


if __name__ == "__main__":
  app.run(debug=True)
