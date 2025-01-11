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

if __name__ == "__main__":
  app.run(debug=True)
