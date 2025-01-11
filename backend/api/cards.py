from flask import Blueprint, jsonify
import requests
import os

# Get API key from .env
API_KEY = os.environ.get("TCG_API_KEY")

card_routes = Blueprint('cards', __name__)

# Route for calling TCG API on a Pokémon
@card_routes.route('/cards/<pokemon_name>', methods=['GET'])
def get_cards(pokemon_name):
  tcgapi_url = f"https://api.pokemontcg.io/v2/cards?q=name:{pokemon_name}"
  # Headers for API
  headers = {"X-Api_Key": API_KEY}
  response = requests.get(tcgapi_url, headers=headers)
  data = response.json()
  return jsonify(data)
# Working
