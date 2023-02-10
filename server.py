import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)



if __name__ == '__main__':
    app.run(port=5000, debug=True)