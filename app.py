from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os
app = Flask(__name__, template_folder='templates')
CORS(app)

DATA_FILE = 'backend/developers.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as F:
        return json.load(F)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

