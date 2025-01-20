from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    names = request.args.getlist('name')
    return names

@app.route('/about')
def about():
    return 'About'