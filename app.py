from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os
app = Flask(__name__, template_folder='templates')
CORS(app)
DATA_FILE = 'backend/developers.json'
