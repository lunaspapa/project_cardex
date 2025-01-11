from flask import Blueprint, jsonify
import requests

pokemon_routes = Blueprint('pokemon', __name__)

# Route for Pokémon API Call
@pokemon_routes.route('/pokemon', methods=['GET'])
def get_pokemon():
  # Fetching Pokémon from Generation I
  gen_i_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
  response = requests.get(gen_i_url)
  data = response.json()
  return jsonify(data)
# Working
