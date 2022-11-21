import flask
from flask import request, jsonify, render_template, Blueprint
import json
import os
import sys
import time

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/dashboard')
def dashboard():
    print("dashboard")
    return render_template('dashboard.html')

if __name__ == '__main__':
   app.run()