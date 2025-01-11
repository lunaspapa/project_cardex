# Imports
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from api.pokemon import pokemon_routes
from api.cards import card_routes

# Initialize
app = Flask(__name__)
app.register_blueprint(pokemon_routes)
app.register_blueprint(card_routes)
CORS(app)

# é (Alt+0233) (For proper stylization of Pokémon)

# Simple home placeholder route
@app.route('/')
def home():
  return jsonify({"message": "Welcome to the Pokémon Card API Backend!"})
# Working


if __name__ == "__main__":
  app.run(debug=True)
