import flask
from flask import request, jsonify, render_template, redirect
import db
import json
import os
import sys
import time

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    
@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    default_value = 'NA'
    phone_number = request.form.get('phone_nunber', default_value)
    print(phone_number)
    try: int(phone_number)
    except: return redirect('/')
    if len(phone_number) < 10 or len(phone_number) > 10:
        print('Invalid phone number') 
        return redirect('/')
    print(f"Logged in with {phone_number}")
    return render_template('dashboard.html', tokens=db.get_tokens(phone_number))

if __name__ == '__main__':
   app.run()